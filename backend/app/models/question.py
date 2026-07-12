from sqlalchemy import Column, Enum, Integer, Text, ForeignKey
from sqlalchemy.orm import relationship
from app.core.enums import QuestionType

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

    question_type = Column(
        Enum(QuestionType),
        nullable=False,
        default=QuestionType.MCQ,
    )

    difficulty = Column(
        Integer,
        nullable=False,
        default=1,
    )

    points = Column(
        Integer,
        nullable=False,
        default=1,
    )

    explanation = Column(
        Text,
        nullable=True,
    )

    hint = Column(
        Text,
        nullable=True,
    )

    quiz = relationship(
        "Quiz",
        back_populates="questions",
    )

    answer_options = relationship(
        "AnswerOption",
        back_populates="question",
        cascade="all, delete-orphan",
    )
