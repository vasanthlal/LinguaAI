from typing import Optional

from fastapi import APIRouter, Depends, Query, status
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.schemas.quiz_attempt import (
    QuizAttemptCreate,
    QuizAttemptResponse,
)
from app.services import quiz_attempt_service

router = APIRouter(
    prefix='/quiz-attempts',
    tags=['Quiz Attempts'],
)


@router.get(
    '/',
    response_model=list[QuizAttemptResponse],
)
def get_quiz_attempts(
    skip: int = Query(
        0,
        ge=0,
        description='Number of records to skip',
    ),
    limit: int = Query(
        10,
        ge=1,
        le=100,
        description='Maximum number of records to return',
    ),
    search: Optional[str] = Query(
        None,
        description='Search by user id',
    ),
    status_filter: Optional[str] = Query(
        None,
        description='Filter by quiz attempt status',
    ),
    sort_by: str = Query(
        'id',
        description='Sort by: id, created_at, score',
    ),
    order: str = Query(
        'desc',
        pattern='^(asc|desc)$',
        description='Sort order',
    ),
    db: Session = Depends(get_db),
):
    return quiz_attempt_service.get_quiz_attempts(
        db=db,
        skip=skip,
        limit=limit,
        search=search,
        status_filter=status_filter,
        sort_by=sort_by,
        order=order,
    )


@router.get(
    '/{attempt_id}',
    response_model=QuizAttemptResponse,
)
def get_quiz_attempt(
    attempt_id: int,
    db: Session = Depends(get_db),
):
    return quiz_attempt_service.get_quiz_attempt(
        db,
        attempt_id,
    )


@router.post(
    '/',
    response_model=QuizAttemptResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_quiz_attempt(
    quiz_attempt: QuizAttemptCreate,
    db: Session = Depends(get_db),
):
    return quiz_attempt_service.create_quiz_attempt(
        db,
        quiz_attempt,
    )