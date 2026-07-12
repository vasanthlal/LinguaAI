from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.exceptions import NotFoundException

from app.database.session import get_db
from app.schemas.question import (
    QuestionCreate,
    QuestionUpdate,
    QuestionResponse,
)
from app.services import question_service

router = APIRouter(
    prefix="/questions",
    tags=["Questions"],
)


@router.get("/", response_model=list[QuestionResponse])
def get_questions(db: Session = Depends(get_db)):
    return question_service.get_questions(db)


@router.get("/{question_id}", response_model=QuestionResponse)
def get_question(question_id: int, db: Session = Depends(get_db)):
    question = question_service.get_question(db, question_id)

    if not question:
        raise HTTPException(
            status_code=404,
            detail="Question not found",
        )

    return question


@router.post(
    "/",
    response_model=QuestionResponse,
    summary="Create a new question",
    description="Create a new question for a quiz.",
    response_description="The newly created question.",
)
def create_question(
    question: QuestionCreate,
    db: Session = Depends(get_db),
):
    return question_service.create_question(db, question)


@router.put("/{question_id}", response_model=QuestionResponse)
def update_question(
    question_id: int,
    question: QuestionUpdate,
    db: Session = Depends(get_db),
):
    updated_question = question_service.update_question(
        db,
        question_id,
        question,
    )

    if not updated_question:
        raise NotFoundException("Question")

    return updated_question


@router.delete("/{question_id}")
def delete_question(
    question_id: int,
    db: Session = Depends(get_db),
):
    deleted_question = question_service.delete_question(
        db,
        question_id,
    )

    if not deleted_question:
        raise NotFoundException("Question")

    return {"message": "Question deleted successfully"}
