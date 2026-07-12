from sqlalchemy import Column, Integer, Text, ForeignKey
from sqlalchemy.orm import relationship

from app.database.base import Base


class Question(Base):
    __tablename__ = "questions"

    id = Column(Integer, primary_key=True, index=True)

    quiz_id = Column(
        Integer,
        ForeignKey("quizzes.id"),
        nullable=False,
    )

    question_text = Column(
        Text,
        nullable=False,
    )

    difficulty = Column(
        Integer,
        nullable=False,
        default=1,
    )

    quiz = relationship(
        "Quiz",
        back_populates="questions",
    )