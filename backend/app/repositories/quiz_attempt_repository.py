from sqlalchemy.orm import Session

from app.models.quiz_attempt import QuizAttempt
from app.schemas.quiz_attempt import QuizAttemptCreate
from datetime import datetime


def get_quiz_attempt(db: Session, attempt_id: int):
    return db.query(QuizAttempt).filter(QuizAttempt.id == attempt_id).first()


def create_quiz_attempt(
    db: Session,
    quiz_attempt: QuizAttemptCreate,
):
    db_attempt = QuizAttempt(**quiz_attempt.model_dump())

    db.add(db_attempt)
    db.commit()
    db.refresh(db_attempt)

    return db_attempt


def update_quiz_attempt(db: Session, quiz_attempt: QuizAttempt):
    db.commit()
    db.refresh(quiz_attempt)

    return quiz_attempt


def complete_quiz_attempt(
    db: Session,
    quiz_attempt: QuizAttempt,
    score: int,
    total_questions: int,
    correct_answers: int,
):
    quiz_attempt.score = score
    quiz_attempt.total_questions = total_questions
    quiz_attempt.correct_answers = correct_answers
    quiz_attempt.status = "COMPLETED"
    quiz_attempt.completed_at = datetime.utcnow()

    db.commit()
    db.refresh(quiz_attempt)

    return quiz_attempt


def create_quiz_attempt_no_commit(
    db: Session,
    quiz_attempt: QuizAttemptCreate,
):
    db_attempt = QuizAttempt(**quiz_attempt.model_dump())

    db.add(db_attempt)
    db.flush()  # gets the generated ID
    db.refresh(db_attempt)

    return db_attempt
