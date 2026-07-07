from sqlalchemy.orm import Session

from app.repositories.user_repository import (
    create_user,
    get_user_by_email,
)
from app.schemas.user import UserCreate


def register_user(
    db: Session,
    user: UserCreate,
):
    existing_user = get_user_by_email(
        db,
        user.email,
    )

    if existing_user:
        raise Exception("Email already registered")

    return create_user(
        db,
        user,
    )