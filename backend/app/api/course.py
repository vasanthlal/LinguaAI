from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.schemas.course import (
    CourseCreate,
    CourseResponse,
    CourseUpdate,
)
from app.services import course_service

router = APIRouter(
    prefix="/courses",
    tags=["Courses"],
)


@router.get(
    "/",
    response_model=list[CourseResponse],
)
def get_courses(
    db: Session = Depends(get_db),
):
    return course_service.get_courses(db)


@router.get(
    "/{course_id}",
    response_model=CourseResponse,
)
def get_course(
    course_id: int,
    db: Session = Depends(get_db),
):
    return course_service.get_course(
        db,
        course_id,
    )


@router.post(
    "/",
    response_model=CourseResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_course(
    course: CourseCreate,
    db: Session = Depends(get_db),
):
    return course_service.create_course(
        db,
        course,
    )


@router.put(
    "/{course_id}",
    response_model=CourseResponse,
)
def update_course(
    course_id: int,
    course: CourseUpdate,
    db: Session = Depends(get_db),
):
    return course_service.update_course(
        db,
        course_id,
        course,
    )


@router.delete(
    "/{course_id}",
)
def delete_course(
    course_id: int,
    db: Session = Depends(get_db),
):
    return course_service.delete_course(
        db,
        course_id,
    )
