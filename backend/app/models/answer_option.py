from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from app.database.base import Base


class AnswerOption(Base):
    __tablename__ = "answer_options"

    id = Column(Integer, primary_key=True, index=True)

    question_id = Column(
        Integer,
        ForeignKey("questions.id"),
        nullable=False,
    )

    option_text = Column(
        String(255),
        nullable=False,
    )

    is_correct = Column(
        Boolean,
        default=False,
        nullable=False,
    )

    display_order = Column(
        Integer,
        nullable=False,
    )

    question = relationship(
        "Question",
        back_populates="answer_options",
    )