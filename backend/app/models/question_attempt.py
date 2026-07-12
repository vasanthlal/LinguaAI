from sqlalchemy import Boolean, Column, ForeignKey, Integer
from sqlalchemy.orm import relationship

from app.database.base import Base


class QuestionAttempt(Base):
    __tablename__ = "question_attempts"

    id = Column(Integer, primary_key=True, index=True)

    quiz_attempt_id = Column(
        Integer,
        ForeignKey("quiz_attempts.id"),
        nullable=False,
    )

    question_id = Column(
        Integer,
        ForeignKey("questions.id"),
        nullable=False,
    )

    selected_answer_option_id = Column(
        Integer,
        ForeignKey("answer_options.id"),
        nullable=False,
    )

    is_correct = Column(
        Boolean,
        nullable=False,
        default=False,
    )

    points_awarded = Column(
        Integer,
        nullable=False,
        default=0,
    )

    quiz_attempt = relationship(
        "QuizAttempt",
        back_populates="question_attempts",
    )

    question = relationship("Question")

    selected_answer_option = relationship("AnswerOption")
