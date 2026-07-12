from sqlalchemy.orm import Session

from app.repositories import answer_option_repository
from app.schemas.answer_option import (
    AnswerOptionCreate,
    AnswerOptionUpdate,
)


def get_answer_options(db: Session):
    return answer_option_repository.get_all_answer_options(db)


def get_answer_option(db: Session, answer_option_id: int):
    return answer_option_repository.get_answer_option_by_id(
        db,
        answer_option_id,
    )


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
    return answer_option_repository.update_answer_option(
        db,
        answer_option_id,
        answer_option,
    )


def delete_answer_option(
    db: Session,
    answer_option_id: int,
):
    return answer_option_repository.delete_answer_option(
        db,
        answer_option_id,
    )