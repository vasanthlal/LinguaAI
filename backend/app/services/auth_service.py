from app.utils.security import (
    create_access_token,
    verify_password,
)
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
def login_user(
    db: Session,
    email: str,
    password: str,
):
    user = get_user_by_email(
        db,
        email,
    )

    if not user:
        raise Exception("Invalid email or password")

    if not verify_password(
        password,
        user.password_hash,
    ):
        raise Exception("Invalid email or password")

    access_token = create_access_token(
        data={
            "sub": user.email,
        }
    )

    return {
        "access_token": access_token,
        "token_type": "bearer",
    }