from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import relationship

from app.database.base import Base


class Lesson(Base):
    __tablename__ = "lessons"

    id = Column(Integer, primary_key=True, index=True)

    course_id = Column(
        Integer,
        ForeignKey("courses.id"),
        nullable=False,
    )

    title = Column(
        String(150),
        nullable=False,
    )

    content = Column(
        Text,
        nullable=False,
    )

    order = Column(
        Integer,
        nullable=False,
    )

    course = relationship(
        "Course",
        back_populates="lessons",
    )