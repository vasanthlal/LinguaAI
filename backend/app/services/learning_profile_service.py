from sqlalchemy.orm import Session

from app.repositories.learning_profile_repository import (
    create_learning_profile,
    get_learning_profile,
)
from app.schemas.learning_profile import LearningProfileCreate


def save_learning_profile(
    db: Session,
    user_id: int,
    profile: LearningProfileCreate,
):
    existing_profile = get_learning_profile(
        db,
        user_id,
    )

    if existing_profile:
        raise Exception(
            "Learning profile already exists."
        )

    return create_learning_profile(
        db,
        user_id,
        profile,
    )