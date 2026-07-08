from sqlalchemy.orm import Session

from app.models.user import User
from app.schemas.user import UserCreate
from app.utils.security import hash_password


def get_user_by_email(
    db: Session,
    email: str,
):
    return (
        db.query(User)
        .filter(User.email == email)
        .first()
    )

def authenticate_user(
    db: Session,
    email: str,
):
    return (
        db.query(User)
        .filter(User.email == email)
        .first()
    )

def create_user(
    db: Session,
    user: UserCreate,
):
    db_user = User(
        full_name=user.full_name,
        email=user.email,
        password_hash=hash_password(user.password),
        native_language=user.native_language,
        target_language=user.target_language,
    )

    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    return db_user