from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.schemas.answer_option import (
    AnswerOptionCreate,
    AnswerOptionUpdate,
    AnswerOptionResponse,
)
from app.services import answer_option_service

router = APIRouter(
    prefix="/answer-options",
    tags=["Answer Options"],
)


@router.get("/", response_model=list[AnswerOptionResponse])
def get_answer_options(db: Session = Depends(get_db)):
    return answer_option_service.get_answer_options(db)


@router.get("/{answer_option_id}", response_model=AnswerOptionResponse)
def get_answer_option(
    answer_option_id: int,
    db: Session = Depends(get_db),
):
    answer_option = answer_option_service.get_answer_option(
        db,
        answer_option_id,
    )

    if not answer_option:
        raise HTTPException(
            status_code=404,
            detail="Answer option not found",
        )

    return answer_option


@router.post("/", response_model=AnswerOptionResponse)
def create_answer_option(
    answer_option: AnswerOptionCreate,
    db: Session = Depends(get_db),
):
    return answer_option_service.create_answer_option(
        db,
        answer_option,
    )


@router.put("/{answer_option_id}", response_model=AnswerOptionResponse)
def update_answer_option(
    answer_option_id: int,
    answer_option: AnswerOptionUpdate,
    db: Session = Depends(get_db),
):
    updated = answer_option_service.update_answer_option(
        db,
        answer_option_id,
        answer_option,
    )

    if not updated:
        raise HTTPException(
            status_code=404,
            detail="Answer option not found",
        )

    return updated


@router.delete("/{answer_option_id}")
def delete_answer_option(
    answer_option_id: int,
    db: Session = Depends(get_db),
):
    deleted = answer_option_service.delete_answer_option(
        db,
        answer_option_id,
    )

    if not deleted:
        raise HTTPException(
            status_code=404,
            detail="Answer option not found",
        )

    return {"message": "Answer option deleted successfully"}
