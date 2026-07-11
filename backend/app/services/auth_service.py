from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.core.logger import logger
from app.repositories.user_repository import (
    create_user,
    get_user_by_email,
)
from app.schemas.user import UserCreate
from app.utils.security import (
    create_access_token,
    verify_password,
)


def register_user(
    db: Session,
    user: UserCreate,
):
    """Register a new user."""

    existing_user = get_user_by_email(
        db,
        user.email,
    )

    if existing_user:
        logger.warning(f"Registration failed: {user.email} already exists")

        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already registered",
        )

    logger.info(f"Creating user: {user.email}")

    return create_user(
        db,
        user,
    )


def login_user(
    db: Session,
    email: str,
    password: str,
):
    """Authenticate user and return JWT token."""

    user = get_user_by_email(
        db,
        email,
    )

    if not user:
        logger.warning(f"Login failed: {email} not found")

        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email or password",
        )

    if not verify_password(
        password,
        user.password_hash,
    ):
        logger.warning(f"Login failed: Incorrect password for {email}")

        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email or password",
        )

    logger.info(f"User logged in successfully: {email}")

    access_token = create_access_token(
        data={
            "sub": user.email,
        }
    )

    return {
        "access_token": access_token,
        "token_type": "bearer",
    }
