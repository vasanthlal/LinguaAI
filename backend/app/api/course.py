from typing import Optional

from fastapi import APIRouter, Depends, Query, status
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
    skip: int = Query(
        0,
        ge=0,
        description="Number of records to skip",
    ),
    limit: int = Query(
        10,
        ge=1,
        le=100,
        description="Maximum number of records to return",
    ),
    search: Optional[str] = Query(
        None,
        description="Search by course title",
    ),
    is_active: Optional[bool] = Query(
        None,
        description="Filter active/inactive courses",
    ),
    sort_by: str = Query(
        "title",
        description="Sort by: id, title",
    ),
    order: str = Query(
        "asc",
        pattern="^(asc|desc)$",
        description="Sort order",
    ),
    db: Session = Depends(get_db),
):
    return course_service.get_courses(
        db=db,
        skip=skip,
        limit=limit,
        search=search,
        is_active=is_active,
        sort_by=sort_by,
        order=order,
    )


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