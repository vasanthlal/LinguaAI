from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.repositories.language_repository import (
    get_all_languages,
    get_language_by_id,
)


def list_languages(db: Session):
    return get_all_languages(db)


def get_language(
    db: Session,
    language_id: int,
):
    language = get_language_by_id(
        db,
        language_id,
    )

    if language is None:
        raise HTTPException(
            status_code=404,
            detail="Language not found",
        )

    return language
