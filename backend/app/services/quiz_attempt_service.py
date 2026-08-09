from typing import Optional

from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.repositories import quiz_attempt_repository
from app.schemas.quiz_attempt import QuizAttemptCreate


def get_quiz_attempts(
    db: Session,
    skip: int = 0,
    limit: int = 10,
    search: Optional[str] = None,
    status_filter: Optional[str] = None,
    sort_by: str = 'id',
    order: str = 'desc',
):
    return quiz_attempt_repository.get_all_quiz_attempts(
        db=db,
        skip=skip,
        limit=limit,
        search=search,
        status_filter=status_filter,
        sort_by=sort_by,
        order=order,
    )


def get_quiz_attempt(
    db: Session,
    attempt_id: int,
):
    attempt = quiz_attempt_repository.get_quiz_attempt(
        db,
        attempt_id,
    )

    if attempt is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Quiz attempt not found',
        )

    return attempt


def create_quiz_attempt(
    db: Session,
    quiz_attempt: QuizAttemptCreate,
):
    return quiz_attempt_repository.create_quiz_attempt(
        db,
        quiz_attempt,
    )