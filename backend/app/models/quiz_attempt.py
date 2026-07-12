from sqlalchemy import Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from app.database.base import Base


class QuizAttempt(Base):
    __tablename__ = "quiz_attempts"

    id = Column(Integer, primary_key=True, index=True)

    user_id = Column(
        Integer,
        ForeignKey("users.id"),
        nullable=False,
    )

    quiz_id = Column(
        Integer,
        ForeignKey("quizzes.id"),
        nullable=False,
    )

    score = Column(
        Integer,
        nullable=False,
        default=0,
    )

    total_questions = Column(
        Integer,
        nullable=False,
        default=0,
    )

    correct_answers = Column(
        Integer,
        nullable=False,
        default=0,
    )

    status = Column(
        String(20),
        nullable=False,
        default="IN_PROGRESS",
    )

    completed_at = Column(
        DateTime,
        nullable=True,
    )

    user = relationship(
        "User",
        back_populates="quiz_attempts",
    )

    quiz = relationship(
        "Quiz",
        back_populates="quiz_attempts",
    )

    question_attempts = relationship(
        "QuestionAttempt",
        back_populates="quiz_attempt",
        cascade="all, delete-orphan",
    )
