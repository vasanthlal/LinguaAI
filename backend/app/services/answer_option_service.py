from typing import Optional

from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.repositories import answer_option_repository
from app.schemas.answer_option import (
    AnswerOptionCreate,
    AnswerOptionUpdate,
)


def get_answer_options(
    db: Session,
    skip: int = 0,
    limit: int = 10,
    search: Optional[str] = None,
    is_active: Optional[bool] = None,
    sort_by: str = "id",
    order: str = "asc",
):
    return answer_option_repository.get_all_answer_options(
        db=db,
        skip=skip,
        limit=limit,
        search=search,
        is_active=is_active,
        sort_by=sort_by,
        order=order,
    )


def get_answer_option(
    db: Session,
    answer_option_id: int,
):
    answer_option = answer_option_repository.get_answer_option_by_id(
        db,
        answer_option_id,
    )

    if answer_option is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Answer option not found",
        )

    return answer_option


def create_answer_option(
    db: Session,
    answer_option: AnswerOptionCreate,
):
    return answer_option_repository.create_answer_option(
        db,
        answer_option,
    )


def update_answer_option(
    db: Session,
    answer_option_id: int,
    answer_option: AnswerOptionUpdate,
):
    updated_answer_option = answer_option_repository.update_answer_option(
        db,
        answer_option_id,
        answer_option,
    )

    if updated_answer_option is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Answer option not found",
        )

    return updated_answer_option


def delete_answer_option(
    db: Session,
    answer_option_id: int,
):
    deleted_answer_option = answer_option_repository.delete_answer_option(
        db,
        answer_option_id,
    )

    if deleted_answer_option is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Answer option not found",
        )

    return {
        "message": "Answer option deleted successfully",
    }