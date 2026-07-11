from sqlalchemy import (
    Column,
    DateTime,
    ForeignKey,
    Integer,
    String,
)
from sqlalchemy.sql import func

from app.database.base import Base


class LearningProfile(Base):
    __tablename__ = "learning_profiles"

    id = Column(
        Integer,
        primary_key=True,
        index=True,
    )

    user_id = Column(
        Integer,
        ForeignKey("users.id"),
        nullable=False,
    )

    native_language = Column(
        String,
        nullable=False,
    )

    target_language = Column(
        String,
        nullable=False,
    )

    current_level = Column(
        String,
        default="A0",
    )

    daily_goal_minutes = Column(
        Integer,
        default=15,
    )

    learning_goal = Column(
        String,
        default="Fluency",
    )

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
    )

    updated_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
    )
