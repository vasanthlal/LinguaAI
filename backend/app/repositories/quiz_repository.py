from typing import Optional

from sqlalchemy import asc, desc
from sqlalchemy.orm import Session

from app.models.quiz import Quiz
from app.schemas.quiz import QuizCreate, QuizUpdate


def get_all_quizzes(
    db: Session,
    skip: int = 0,
    limit: int = 10,
    search: Optional[str] = None,
    is_active: Optional[bool] = None,
    sort_by: str = "title",
    order: str = "asc",
):
    query = db.query(Quiz)

    if search:
        query = query.filter(Quiz.title.ilike(f"%{search}%"))

    if is_active is not None and hasattr(Quiz, "is_active"):
        query = query.filter(Quiz.is_active == is_active)

    sort_columns = {
        "id": Quiz.id,
        "title": Quiz.title,
    }

    if hasattr(Quiz, "lesson_id"):
        sort_columns["lesson_id"] = Quiz.lesson_id

    sort_column = sort_columns.get(sort_by, Quiz.title)

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


def get_quiz_by_id(
    db: Session,
    quiz_id: int,
):
    return db.query(Quiz).filter(Quiz.id == quiz_id).first()


def create_quiz(
    db: Session,
    quiz: QuizCreate,
):
    db_quiz = Quiz(**quiz.model_dump())

    db.add(db_quiz)
    db.commit()
    db.refresh(db_quiz)

    return db_quiz


def update_quiz(
    db: Session,
    quiz_id: int,
    quiz: QuizUpdate,
):
    db_quiz = get_quiz_by_id(
        db,
        quiz_id,
    )

    if not db_quiz:
        return None

    update_data = quiz.model_dump(exclude_unset=True)

    for key, value in update_data.items():
        setattr(db_quiz, key, value)

    db.commit()
    db.refresh(db_quiz)

    return db_quiz


def delete_quiz(
    db: Session,
    quiz_id: int,
):
    db_quiz = get_quiz_by_id(
        db,
        quiz_id,
    )

    if not db_quiz:
        return None

    db.delete(db_quiz)
    db.commit()

    return db_quiz