from typing import Optional

from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.repositories import course_repository
from app.schemas.course import CourseCreate, CourseUpdate


def get_courses(
    db: Session,
    skip: int = 0,
    limit: int = 10,
    search: Optional[str] = None,
    is_active: Optional[bool] = None,
    sort_by: str = "title",
    order: str = "asc",
):
    return course_repository.get_all_courses(
        db=db,
        skip=skip,
        limit=limit,
        search=search,
        is_active=is_active,
        sort_by=sort_by,
        order=order,
    )


def get_course(
    db: Session,
    course_id: int,
):
    course = course_repository.get_course_by_id(
        db,
        course_id,
    )

    if course is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Course not found",
        )

    return course


def create_course(
    db: Session,
    course: CourseCreate,
):
    return course_repository.create_course(
        db,
        course,
    )


def update_course(
    db: Session,
    course_id: int,
    course: CourseUpdate,
):
    db_course = course_repository.update_course(
        db,
        course_id,
        course,
    )

    if db_course is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Course not found",
        )

    return db_course


def delete_course(
    db: Session,
    course_id: int,
):
    db_course = course_repository.delete_course(
        db,
        course_id,
    )

    if db_course is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Course not found",
        )

    return {
        "message": "Course deleted successfully",
    }