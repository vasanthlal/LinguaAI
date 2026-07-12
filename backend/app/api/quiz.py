from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.schemas.quiz import (
    QuizCreate,
    QuizUpdate,
    QuizResponse,
)
from app.services import quiz_service

router = APIRouter(
    prefix="/quizzes",
    tags=["Quizzes"],
)


@router.get("/", response_model=list[QuizResponse])
def get_quizzes(db: Session = Depends(get_db)):
    return quiz_service.get_quizzes(db)


@router.get("/{quiz_id}", response_model=QuizResponse)
def get_quiz(quiz_id: int, db: Session = Depends(get_db)):
    quiz = quiz_service.get_quiz(db, quiz_id)

    if not quiz:
        raise HTTPException(status_code=404, detail="Quiz not found")

    return quiz


@router.post("/", response_model=QuizResponse)
def create_quiz(
    quiz: QuizCreate,
    db: Session = Depends(get_db),
):
    return quiz_service.create_quiz(db, quiz)


@router.put("/{quiz_id}", response_model=QuizResponse)
def update_quiz(
    quiz_id: int,
    quiz: QuizUpdate,
    db: Session = Depends(get_db),
):
    updated_quiz = quiz_service.update_quiz(
        db,
        quiz_id,
        quiz,
    )

    if not updated_quiz:
        raise HTTPException(status_code=404, detail="Quiz not found")

    return updated_quiz


@router.delete("/{quiz_id}")
def delete_quiz(
    quiz_id: int,
    db: Session = Depends(get_db),
):
    deleted_quiz = quiz_service.delete_quiz(
        db,
        quiz_id,
    )

    if not deleted_quiz:
        raise HTTPException(status_code=404, detail="Quiz not found")

    return {
        "message": "Quiz deleted successfully"
    }