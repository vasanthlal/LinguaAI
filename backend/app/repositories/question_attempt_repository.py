from sqlalchemy.orm import Session

from app.models.question_attempt import QuestionAttempt
from app.schemas.question_attempt import QuestionAttemptCreate


def create_question_attempt(
    db: Session,
    question_attempt: QuestionAttemptCreate,
):
    db_attempt = QuestionAttempt(**question_attempt.model_dump())

    db.add(db_attempt)
    db.commit()
    db.refresh(db_attempt)

    return db_attempt


def get_question_attempts_by_quiz_attempt(
    db: Session,
    quiz_attempt_id: int,
):
    return (
        db.query(QuestionAttempt)
        .filter(QuestionAttempt.quiz_attempt_id == quiz_attempt_id)
        .all()
    )


def create_question_attempts(
    db: Session,
    question_attempts: list[QuestionAttempt],
):
    db.add_all(question_attempts)
    db.commit()

    for attempt in question_attempts:
        db.refresh(attempt)

    return question_attempts


def create_question_attempts_no_commit(
    db: Session,
    question_attempts: list[QuestionAttempt],
):
    db.add_all(question_attempts)

    db.flush()

    return question_attempts
