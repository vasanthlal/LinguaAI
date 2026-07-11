from sqlalchemy.orm import Session

from app.repositories import lesson_repository
from app.schemas.lesson import LessonCreate, LessonUpdate


def get_lessons(db: Session):
    return lesson_repository.get_all_lessons(db)


def get_lesson(db: Session, lesson_id: int):
    return lesson_repository.get_lesson_by_id(db, lesson_id)


def create_lesson(db: Session, lesson: LessonCreate):
    return lesson_repository.create_lesson(db, lesson)


def update_lesson(db: Session, lesson_id: int, lesson: LessonUpdate):
    return lesson_repository.update_lesson(db, lesson_id, lesson)


def delete_lesson(db: Session, lesson_id: int):
    return lesson_repository.delete_lesson(db, lesson_id)