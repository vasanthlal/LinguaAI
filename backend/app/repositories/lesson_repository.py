from typing import Optional

from sqlalchemy import asc, desc
from sqlalchemy.orm import Session

from app.models.lesson import Lesson
from app.schemas.lesson import LessonCreate, LessonUpdate


def get_all_lessons(
    db: Session,
    skip: int = 0,
    limit: int = 10,
    search: Optional[str] = None,
    is_active: Optional[bool] = None,
    sort_by: str = "title",
    order: str = "asc",
):
    query = db.query(Lesson)

    if search:
        query = query.filter(Lesson.title.ilike(f"%{search}%"))

    if is_active is not None and hasattr(Lesson, "is_active"):
        query = query.filter(Lesson.is_active == is_active)

    sort_columns = {
        "id": Lesson.id,
        "title": Lesson.title,
    }

    if hasattr(Lesson, "course_id"):
        sort_columns["course_id"] = Lesson.course_id

    sort_column = sort_columns.get(sort_by, Lesson.title)

    if order.lower() == "desc":
        query = query.order_by(desc(sort_column))
    else:
        query = query.order_by(asc(sort_column))

    return (
        query
        .offset(skip)
        .limit(limit)
        .all()
    )


def get_lesson_by_id(
    db: Session,
    lesson_id: int,
):
    return db.query(Lesson).filter(Lesson.id == lesson_id).first()


def create_lesson(
    db: Session,
    lesson: LessonCreate,
):
    db_lesson = Lesson(**lesson.model_dump())

    db.add(db_lesson)
    db.commit()
    db.refresh(db_lesson)

    return db_lesson


def update_lesson(
    db: Session,
    lesson_id: int,
    lesson: LessonUpdate,
):
    db_lesson = get_lesson_by_id(
        db,
        lesson_id,
    )

    if not db_lesson:
        return None

    update_data = lesson.model_dump(exclude_unset=True)

    for key, value in update_data.items():
        setattr(db_lesson, key, value)

    db.commit()
    db.refresh(db_lesson)

    return db_lesson


def delete_lesson(
    db: Session,
    lesson_id: int,
):
    db_lesson = get_lesson_by_id(
        db,
        lesson_id,
    )

    if not db_lesson:
        return None

    db.delete(db_lesson)
    db.commit()

    return db_lesson