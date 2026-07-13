from sqlalchemy.orm import Session

from app.models.language import Language
from app.schemas.language import LanguageCreate, LanguageUpdate


def get_all_languages(db: Session):
    return db.query(Language).filter(Language.is_active).order_by(Language.name).all()


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
