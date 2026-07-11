from sqlalchemy.orm import Session

from app.models.lesson import Lesson
from app.schemas.lesson import LessonCreate, LessonUpdate


def get_all_lessons(db: Session):
    return db.query(Lesson).all()


def get_lesson_by_id(db: Session, lesson_id: int):
    return db.query(Lesson).filter(Lesson.id == lesson_id).first()


def create_lesson(db: Session, lesson: LessonCreate):
    db_lesson = Lesson(**lesson.model_dump())

    db.add(db_lesson)
    db.commit()
    db.refresh(db_lesson)

    return db_lesson


def update_lesson(db: Session, lesson_id: int, lesson: LessonUpdate):
    db_lesson = get_lesson_by_id(db, lesson_id)

    if not db_lesson:
        return None

    update_data = lesson.model_dump(exclude_unset=True)

    for key, value in update_data.items():
        setattr(db_lesson, key, value)

    db.commit()
    db.refresh(db_lesson)

    return db_lesson


def delete_lesson(db: Session, lesson_id: int):
    db_lesson = get_lesson_by_id(db, lesson_id)

    if not db_lesson:
        return None

    db.delete(db_lesson)
    db.commit()

    return db_lesson
