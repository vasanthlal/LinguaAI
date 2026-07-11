from sqlalchemy.orm import Session

from app.repositories import course_repository
from app.schemas.course import CourseCreate, CourseUpdate


def get_courses(db: Session):
    return course_repository.get_all_courses(db)


def get_course(db: Session, course_id: int):
    return course_repository.get_course_by_id(db, course_id)


def create_course(db: Session, course: CourseCreate):
    return course_repository.create_course(db, course)


def update_course(db: Session, course_id: int, course: CourseUpdate):
    return course_repository.update_course(db, course_id, course)


def delete_course(db: Session, course_id: int):
    return course_repository.delete_course(db, course_id)