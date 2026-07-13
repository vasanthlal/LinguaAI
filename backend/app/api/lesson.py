from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.schemas.lesson import (
    LessonCreate,
    LessonResponse,
    LessonUpdate,
)
from app.services import lesson_service

router = APIRouter(
    prefix="/lessons",
    tags=["Lessons"],
)


@router.get(
    "/",
    response_model=list[LessonResponse],
)
def get_lessons(
    db: Session = Depends(get_db),
):
    return lesson_service.get_lessons(db)


@router.get(
    "/{lesson_id}",
    response_model=LessonResponse,
)
def get_lesson(
    lesson_id: int,
    db: Session = Depends(get_db),
):
    return lesson_service.get_lesson(
        db,
        lesson_id,
    )


@router.post(
    "/",
    response_model=LessonResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_lesson(
    lesson: LessonCreate,
    db: Session = Depends(get_db),
):
    return lesson_service.create_lesson(
        db,
        lesson,
    )


@router.put(
    "/{lesson_id}",
    response_model=LessonResponse,
)
def update_lesson(
    lesson_id: int,
    lesson: LessonUpdate,
    db: Session = Depends(get_db),
):
    return lesson_service.update_lesson(
        db,
        lesson_id,
        lesson,
    )


@router.delete(
    "/{lesson_id}",
)
def delete_lesson(
    lesson_id: int,
    db: Session = Depends(get_db),
):
    return lesson_service.delete_lesson(
        db,
        lesson_id,
    )
