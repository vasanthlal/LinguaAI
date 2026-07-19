from typing import Optional

from sqlalchemy import asc, desc
from sqlalchemy.orm import Session

from app.models.course import Course
from app.schemas.course import CourseCreate, CourseUpdate


def get_all_courses(
    db: Session,
    skip: int = 0,
    limit: int = 10,
    search: Optional[str] = None,
    is_active: Optional[bool] = None,
    sort_by: str = "title",
    order: str = "asc",
):
    query = db.query(Course)

    if search:
        query = query.filter(Course.title.ilike(f"%{search}%"))

    if is_active is not None and hasattr(Course, "is_active"):
        query = query.filter(Course.is_active == is_active)

    sort_columns = {
        "id": Course.id,
        "title": Course.title,
    }

    # Add these only if your Course model has them
    if hasattr(Course, "language_id"):
        sort_columns["language_id"] = Course.language_id

    sort_column = sort_columns.get(sort_by, Course.title)

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


def get_course_by_id(
    db: Session,
    course_id: int,
):
    return db.query(Course).filter(Course.id == course_id).first()


def create_course(
    db: Session,
    course: CourseCreate,
):
    db_course = Course(**course.model_dump())

    db.add(db_course)
    db.commit()
    db.refresh(db_course)

    return db_course


def update_course(
    db: Session,
    course_id: int,
    course: CourseUpdate,
):
    db_course = get_course_by_id(
        db,
        course_id,
    )

    if not db_course:
        return None

    update_data = course.model_dump(exclude_unset=True)

    for key, value in update_data.items():
        setattr(db_course, key, value)

    db.commit()
    db.refresh(db_course)

    return db_course


def delete_course(
    db: Session,
    course_id: int,
):
    db_course = get_course_by_id(
        db,
        course_id,
    )

    if not db_course:
        return None

    db.delete(db_course)
    db.commit()

    return db_course