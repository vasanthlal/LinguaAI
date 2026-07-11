from sqlalchemy.orm import Session

from app.models.language import Language


def get_all_languages(db: Session):
    return (
        db.query(Language)
        .filter(Language.is_active)
        .order_by(Language.name)
        .all()
    )


def get_language_by_id(
    db: Session,
    language_id: int,
):
    return db.query(Language).filter(Language.id == language_id).first()
