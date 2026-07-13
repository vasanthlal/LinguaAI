from fastapi import HTTPException, status
from sqlalchemy.orm import Session

# from app.models.language import Language
from app.repositories.language_repository import (
    create_language,
    delete_language,
    get_all_languages,
    get_language_by_code,
    get_language_by_id,
    update_language,
)
from app.schemas.language import (
    LanguageCreate,
    LanguageUpdate,
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
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Language not found",
        )

    return language


def create_new_language(
    db: Session,
    language: LanguageCreate,
):
    existing = get_language_by_code(
        db,
        language.code,
    )

    if existing:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Language code already exists",
        )

    return create_language(
        db,
        language,
    )


def update_existing_language(
    db: Session,
    language_id: int,
    language: LanguageUpdate,
):
    db_language = get_language_by_id(
        db,
        language_id,
    )

    if db_language is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Language not found",
        )

    existing = get_language_by_code(
        db,
        language.code,
    )

    if existing and existing.id != language_id:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Language code already exists",
        )

    return update_language(
        db,
        db_language,
        language,
    )


def delete_existing_language(
    db: Session,
    language_id: int,
):
    db_language = get_language_by_id(
        db,
        language_id,
    )

    if db_language is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Language not found",
        )

    delete_language(
        db,
        db_language,
    )

    return {
        "message": "Language deleted successfully",
    }
