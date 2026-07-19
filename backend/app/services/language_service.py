from typing import Optional

from sqlalchemy.orm import Session

from app.core.exceptions import BadRequestException, NotFoundException
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


def list_languages(
    db: Session,
    skip: int = 0,
    limit: int = 10,
    search: Optional[str] = None,
    is_active: Optional[bool] = None,
):
    return get_all_languages(
        db=db,
        skip=skip,
        limit=limit,
        search=search,
        is_active=is_active,
    )


def get_language(
    db: Session,
    language_id: int,
):
    language = get_language_by_id(
        db,
        language_id,
    )

    if language is None:
        raise NotFoundException("Language not found")

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
        raise BadRequestException("Language code already exists")

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
        raise NotFoundException("Language not found")

    existing = get_language_by_code(
        db,
        language.code,
    )

    if existing and existing.id != language_id:
        raise BadRequestException("Language code already exists")

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
        raise NotFoundException("Language not found")

    delete_language(
        db,
        db_language,
    )

    return {
        "message": "Language deleted successfully",
    }