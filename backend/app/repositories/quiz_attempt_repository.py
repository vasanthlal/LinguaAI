from datetime import datetime
from typing import Optional

from sqlalchemy import asc, desc
from sqlalchemy.orm import Session

from app.models.quiz_attempt import QuizAttempt
from app.schemas.quiz_attempt import QuizAttemptCreate


def get_all_quiz_attempts(
    db: Session,
    skip: int = 0,
    limit: int = 10,
    search: Optional[str] = None,
    status_filter: Optional[str] = None,
    sort_by: str = 'id',
    order: str = 'desc',
):
    query = db.query(QuizAttempt)

    # Search by user_id if available
    if search and hasattr(QuizAttempt, 'user_id'):
        query = query.filter(
            QuizAttempt.user_id.cast(str).ilike(f'%{search}%')
        )

    # Filter by status if available
    if status_filter is not None and hasattr(QuizAttempt, 'status'):
        query = query.filter(
            QuizAttempt.status == status_filter
        )

    sort_columns = {
        'id': QuizAttempt.id,
    }

    if hasattr(QuizAttempt, 'created_at'):
        sort_columns['created_at'] = QuizAttempt.created_at

    if hasattr(QuizAttempt, 'score'):
        sort_columns['score'] = QuizAttempt.score

    sort_column = sort_columns.get(sort_by, QuizAttempt.id)

    if order.lower() == 'asc':
        query = query.order_by(asc(sort_column))
    else:
        query = query.order_by(desc(sort_column))

    return (
        query
        .offset(skip)
        .limit(limit)
        .all()
    )


def get_quiz_attempt(
    db: Session,
    attempt_id: int,
):
    return (
        db.query(QuizAttempt)
        .filter(QuizAttempt.id == attempt_id)
        .first()
    )


def create_quiz_attempt(
    db: Session,
    quiz_attempt: QuizAttemptCreate,
):
    db_attempt = QuizAttempt(**quiz_attempt.model_dump())

    db.add(db_attempt)
    db.commit()
    db.refresh(db_attempt)

    return db_attempt


def update_quiz_attempt(
    db: Session,
    quiz_attempt: QuizAttempt,
):
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
    quiz_attempt.status = 'COMPLETED'
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
    db.flush()
    db.refresh(db_attempt)

    return db_attempt