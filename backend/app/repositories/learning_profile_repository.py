from sqlalchemy.orm import Session

from app.models.learning_profile import LearningProfile
from app.schemas.learning_profile import LearningProfileCreate


def create_learning_profile(
    db: Session,
    user_id: int,
    profile: LearningProfileCreate,
):
    db_profile = LearningProfile(
        user_id=user_id,
        native_language=profile.native_language,
        target_language=profile.target_language,
        current_level=profile.current_level,
        daily_goal_minutes=profile.daily_goal_minutes,
        learning_goal=profile.learning_goal,
    )

    db.add(db_profile)
    db.commit()
    db.refresh(db_profile)

    return db_profile


def get_learning_profile(
    db: Session,
    user_id: int,
):
    return (
        db.query(LearningProfile)
        .filter(LearningProfile.user_id == user_id)
        .first()
    )