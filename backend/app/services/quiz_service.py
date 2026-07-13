from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.repositories import quiz_repository
from app.schemas.quiz import QuizCreate, QuizUpdate


def get_quizzes(db: Session):
    return quiz_repository.get_all_quizzes(db)


def get_quiz(
    db: Session,
    quiz_id: int,
):
    quiz = quiz_repository.get_quiz_by_id(
        db,
        quiz_id,
    )

    if quiz is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Quiz not found",
        )

    return quiz


def create_quiz(
    db: Session,
    quiz: QuizCreate,
):
    return quiz_repository.create_quiz(
        db,
        quiz,
    )


def update_quiz(
    db: Session,
    quiz_id: int,
    quiz: QuizUpdate,
):
    updated_quiz = quiz_repository.update_quiz(
        db,
        quiz_id,
        quiz,
    )

    if updated_quiz is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Quiz not found",
        )

    return updated_quiz


def delete_quiz(
    db: Session,
    quiz_id: int,
):
    deleted_quiz = quiz_repository.delete_quiz(
        db,
        quiz_id,
    )

    if deleted_quiz is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Quiz not found",
        )

    return {
        "message": "Quiz deleted successfully",
    }
