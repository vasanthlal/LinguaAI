from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.schemas.quiz_submission import (
    QuizSubmission,
    QuizResult,
)
from app.services.scoring_service import evaluate_quiz

router = APIRouter(
    prefix="/quiz-attempts",
    tags=["Quiz Attempts"],
)


@router.post(
    "/submit",
    response_model=QuizResult,
    summary="Submit a completed quiz",
)
def submit_quiz(
    submission: QuizSubmission,
    db: Session = Depends(get_db),
):
    return evaluate_quiz(
        db,
        submission,
    )
