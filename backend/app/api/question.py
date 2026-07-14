from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.schemas.question import (
    QuestionCreate,
    QuestionResponse,
    QuestionUpdate,
)
from app.services import question_service

router = APIRouter(
    prefix="/questions",
    tags=["Questions"],
)


@router.get(
    "/",
    response_model=list[QuestionResponse],
)
def get_questions(
    db: Session = Depends(get_db),
):
    return question_service.get_questions(db)


@router.get(
    "/{question_id}",
    response_model=QuestionResponse,
)
def get_question(
    question_id: int,
    db: Session = Depends(get_db),
):
    return question_service.get_question(
        db,
        question_id,
    )


@router.post(
    "/",
    response_model=QuestionResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Create a new question",
    description="Create a new question for a quiz.",
    response_description="The newly created question.",
)
def create_question(
    question: QuestionCreate,
    db: Session = Depends(get_db),
):
    return question_service.create_question(
        db,
        question,
    )


@router.put(
    "/{question_id}",
    response_model=QuestionResponse,
)
def update_question(
    question_id: int,
    question: QuestionUpdate,
    db: Session = Depends(get_db),
):
    return question_service.update_question(
        db,
        question_id,
        question,
    )


@router.delete(
    "/{question_id}",
)
def delete_question(
    question_id: int,
    db: Session = Depends(get_db),
):
    return question_service.delete_question(
        db,
        question_id,
    )
