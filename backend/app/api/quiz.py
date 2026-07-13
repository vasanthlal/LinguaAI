from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.schemas.quiz import (
    QuizCreate,
    QuizResponse,
    QuizUpdate,
)
from app.services import quiz_service

router = APIRouter(
    prefix="/quizzes",
    tags=["Quizzes"],
)


@router.get(
    "/",
    response_model=list[QuizResponse],
)
def get_quizzes(
    db: Session = Depends(get_db),
):
    return quiz_service.get_quizzes(db)


@router.get(
    "/{quiz_id}",
    response_model=QuizResponse,
)
def get_quiz(
    quiz_id: int,
    db: Session = Depends(get_db),
):
    return quiz_service.get_quiz(
        db,
        quiz_id,
    )


@router.post(
    "/",
    response_model=QuizResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_quiz(
    quiz: QuizCreate,
    db: Session = Depends(get_db),
):
    return quiz_service.create_quiz(
        db,
        quiz,
    )


@router.put(
    "/{quiz_id}",
    response_model=QuizResponse,
)
def update_quiz(
    quiz_id: int,
    quiz: QuizUpdate,
    db: Session = Depends(get_db),
):
    return quiz_service.update_quiz(
        db,
        quiz_id,
        quiz,
    )


@router.delete(
    "/{quiz_id}",
)
def delete_quiz(
    quiz_id: int,
    db: Session = Depends(get_db),
):
    return quiz_service.delete_quiz(
        db,
        quiz_id,
    )
