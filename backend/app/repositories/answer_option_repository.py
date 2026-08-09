from typing import Optional

from sqlalchemy import asc, desc
from sqlalchemy.orm import Session

from app.models.answer_option import AnswerOption
from app.schemas.answer_option import (
    AnswerOptionCreate,
    AnswerOptionUpdate,
)


def get_all_answer_options(
    db: Session,
    skip: int = 0,
    limit: int = 10,
    search: Optional[str] = None,
    is_active: Optional[bool] = None,
    sort_by: str = "id",
    order: str = "asc",
):
    query = db.query(AnswerOption)

    # Search by option text (if your model has "text")
    if search and hasattr(AnswerOption, "text"):
        query = query.filter(
            AnswerOption.text.ilike(f"%{search}%")
        )

    # Filter active (only if model contains is_active)
    if is_active is not None and hasattr(AnswerOption, "is_active"):
        query = query.filter(
            AnswerOption.is_active == is_active
        )

    sort_columns = {
        "id": AnswerOption.id,
    }

    if hasattr(AnswerOption, "text"):
        sort_columns["text"] = AnswerOption.text

    if hasattr(AnswerOption, "question_id"):
        sort_columns["question_id"] = AnswerOption.question_id

    sort_column = sort_columns.get(
        sort_by,
        AnswerOption.id,
    )

    if order.lower() == "desc":
        query = query.order_by(desc(sort_column))
    else:
        query = query.order_by(asc(sort_column))

    return (
        query
        .offset(skip)
        .limit(limit)
        .all()
    )


def get_answer_option_by_id(
    db: Session,
    answer_option_id: int,
):
    return (
        db.query(AnswerOption)
        .filter(AnswerOption.id == answer_option_id)
        .first()
    )


def create_answer_option(
    db: Session,
    answer_option: AnswerOptionCreate,
):
    db_answer_option = AnswerOption(
        **answer_option.model_dump()
    )

    db.add(db_answer_option)
    db.commit()
    db.refresh(db_answer_option)

    return db_answer_option


def update_answer_option(
    db: Session,
    answer_option_id: int,
    answer_option: AnswerOptionUpdate,
):
    db_answer_option = get_answer_option_by_id(
        db,
        answer_option_id,
    )

    if not db_answer_option:
        return None

    update_data = answer_option.model_dump(
        exclude_unset=True
    )

    for key, value in update_data.items():
        setattr(
            db_answer_option,
            key,
            value,
        )

    db.commit()
    db.refresh(db_answer_option)

    return db_answer_option


def delete_answer_option(
    db: Session,
    answer_option_id: int,
):
    db_answer_option = get_answer_option_by_id(
        db,
        answer_option_id,
    )

    if not db_answer_option:
        return None

    db.delete(db_answer_option)
    db.commit()

    return db_answer_option