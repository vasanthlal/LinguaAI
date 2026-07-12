from sqlalchemy.orm import Session

from app.models.answer_option import AnswerOption
from app.schemas.answer_option import (
    AnswerOptionCreate,
    AnswerOptionUpdate,
)


def get_all_answer_options(db: Session):
    return db.query(AnswerOption).all()


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
    db_answer_option = AnswerOption(**answer_option.model_dump())

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

    update_data = answer_option.model_dump(exclude_unset=True)

    for key, value in update_data.items():
        setattr(db_answer_option, key, value)

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