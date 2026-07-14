from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.repositories import question_repository
from app.schemas.question import QuestionCreate, QuestionUpdate


def get_questions(db: Session):
    return question_repository.get_all_questions(db)


def get_question(
    db: Session,
    question_id: int,
):
    question = question_repository.get_question_by_id(
        db,
        question_id,
    )

    if question is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Question not found",
        )

    return question


def create_question(
    db: Session,
    question: QuestionCreate,
):
    return question_repository.create_question(
        db,
        question,
    )


def update_question(
    db: Session,
    question_id: int,
    question: QuestionUpdate,
):
    updated_question = question_repository.update_question(
        db,
        question_id,
        question,
    )

    if updated_question is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Question not found",
        )

    return updated_question


def delete_question(
    db: Session,
    question_id: int,
):
    deleted_question = question_repository.delete_question(
        db,
        question_id,
    )

    if deleted_question is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Question not found",
        )

    return {
        "message": "Question deleted successfully",
    }
