from typing import Optional

from sqlalchemy.orm import Session

from app.models.language import Language
from app.schemas.language import LanguageCreate, LanguageUpdate


def get_all_languages(
    db: Session,
    skip: int = 0,
    limit: int = 10,
    search: Optional[str] = None,
    is_active: Optional[bool] = None,
):
    query = db.query(Language)

    if search:
        query = query.filter(Language.name.ilike(f"%{search}%"))

    if is_active is not None:
        query = query.filter(Language.is_active == is_active)

    return (
        query.order_by(Language.name)
        .offset(skip)
        .limit(limit)
        .all()
    )


def get_language_by_id(
    db: Session,
    language_id: int,
):
    return db.query(Language).filter(Language.id == language_id).first()


def get_language_by_code(
    db: Session,
    code: str,
):
    return db.query(Language).filter(Language.code == code).first()


def create_language(
    db: Session,
    language: LanguageCreate,
):
    db_language = Language(
        name=language.name,
        code=language.code,
        is_active=language.is_active,
    )

    db.add(db_language)
    db.commit()
    db.refresh(db_language)

    return db_language


def update_language(
    db: Session,
    db_language: Language,
    language: LanguageUpdate,
):
    db_language.name = language.name
    db_language.code = language.code
    db_language.is_active = language.is_active

    db.commit()
    db.refresh(db_language)

    return db_language


def delete_language(
    db: Session,
    db_language: Language,
):
    db.delete(db_language)
    db.commit()