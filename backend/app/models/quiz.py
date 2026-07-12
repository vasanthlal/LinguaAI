from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from app.database.base import Base


class Quiz(Base):
    __tablename__ = "quizzes"

    id = Column(Integer, primary_key=True, index=True)

    lesson_id = Column(
        Integer,
        ForeignKey("lessons.id"),
        nullable=False,
    )

    title = Column(
        String(150),
        nullable=False,
    )

    passing_score = Column(
        Integer,
        nullable=False,
        default=70,
    )

    lesson = relationship(
        "Lesson",
        back_populates="quizzes",
    )

    questions = relationship(
    "Question",
    back_populates="quiz",
    cascade="all, delete-orphan",
    )