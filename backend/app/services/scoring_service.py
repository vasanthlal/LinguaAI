from sqlalchemy.orm import Session

from app.database.unit_of_work import UnitOfWork
from app.models.question_attempt import QuestionAttempt
from app.repositories import (
    answer_option_repository,
    question_attempt_repository,
    question_repository,
    quiz_attempt_repository,
)
from app.schemas.quiz_attempt import QuizAttemptCreate
from app.schemas.quiz_submission import (
    QuizResult,
    QuizSubmission,
)


def evaluate_quiz(
    db: Session,
    submission: QuizSubmission,
) -> QuizResult:
    """
    Evaluate a submitted quiz.
    """

    score = 0
    correct_answers = 0

    results = []
    question_attempts = []

    with UnitOfWork(db):

        quiz_attempt = quiz_attempt_repository.create_quiz_attempt_no_commit(
            db,
            QuizAttemptCreate(
                user_id=submission.user_id,
                quiz_id=submission.quiz_id,
            ),
        )

        for answer in submission.answers:

            question = question_repository.get_question_by_id(
                db,
                answer.question_id,
            )

            if question is None:
                continue

            correct_answer = answer_option_repository.get_correct_answer(
                db,
                answer.question_id,
            )

            if correct_answer is None:
                continue

            is_correct = answer.selected_answer_option_id == correct_answer.id

            points_awarded = 0

            if is_correct:
                points_awarded = question.points
                score += points_awarded
                correct_answers += 1

            question_attempts.append(
                QuestionAttempt(
                    quiz_attempt_id=quiz_attempt.id,
                    question_id=question.id,
                    selected_answer_option_id=answer.selected_answer_option_id,
                    is_correct=is_correct,
                    points_awarded=points_awarded,
                )
            )

            results.append(
                {
                    "question_id": question.id,
                    "selected_answer_option_id": answer.selected_answer_option_id,
                    "correct_answer_option_id": correct_answer.id,
                    "is_correct": is_correct,
                    "points_awarded": points_awarded,
                    "explanation": question.explanation,
                }
            )

        total_questions = len(submission.answers)
        incorrect_answers = total_questions - correct_answers

        percentage = (
            (correct_answers / total_questions) * 100 if total_questions > 0 else 0
        )

        passed = percentage >= 60

        question_attempt_repository.create_question_attempts_no_commit(
            db,
            question_attempts,
        )

        quiz_attempt_repository.complete_quiz_attempt_no_commit(
            db,
            quiz_attempt,
            score,
            total_questions,
            correct_answers,
        )

    return QuizResult(
        quiz_attempt_id=quiz_attempt.id,
        score=score,
        total_questions=total_questions,
        correct_answers=correct_answers,
        incorrect_answers=incorrect_answers,
        percentage=percentage,
        passed=passed,
        time_taken_seconds=0,
        results=results,
    )
