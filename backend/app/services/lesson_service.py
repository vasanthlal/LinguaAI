from typing import Optional

from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.repositories import lesson_repository
from app.schemas.lesson import LessonCreate, LessonUpdate


def get_lessons(
    db: Session,
    skip: int = 0,
    limit: int = 10,
    search: Optional[str] = None,
    is_active: Optional[bool] = None,
    sort_by: str = "title",
    order: str = "asc",
):
    return lesson_repository.get_all_lessons(
        db=db,
        skip=skip,
        limit=limit,
        search=search,
        is_active=is_active,
        sort_by=sort_by,
        order=order,
    )


def get_lesson(
    db: Session,
    lesson_id: int,
):
    lesson = lesson_repository.get_lesson_by_id(
        db,
        lesson_id,
    )

    if lesson is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Lesson not found",
        )

    return lesson


def create_lesson(
    db: Session,
    lesson: LessonCreate,
):
    return lesson_repository.create_lesson(
        db,
        lesson,
    )


def update_lesson(
    db: Session,
    lesson_id: int,
    lesson: LessonUpdate,
):
    updated_lesson = lesson_repository.update_lesson(
        db,
        lesson_id,
        lesson,
    )

    if updated_lesson is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Lesson not found",
        )

    return updated_lesson


def delete_lesson(
    db: Session,
    lesson_id: int,
):
    deleted_lesson = lesson_repository.delete_lesson(
        db,
        lesson_id,
    )

    if deleted_lesson is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Lesson not found",
        )

    return {
        "message": "Lesson deleted successfully",
    }