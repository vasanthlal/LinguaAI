from typing import Optional

from sqlalchemy import asc, desc
from sqlalchemy.orm import Session

from app.models.answer_option import AnswerOption
from app.models.question import Question
from app.schemas.question import QuestionCreate, QuestionUpdate


def get_all_questions(
    db: Session,
    skip: int = 0,
    limit: int = 10,
    search: Optional[str] = None,
    is_active: Optional[bool] = None,
    sort_by: str = "id",
    order: str = "asc",
):
    query = db.query(Question)

    # Update "text" if your Question model uses another field
    if search and hasattr(Question, "text"):
        query = query.filter(Question.text.ilike(f"%{search}%"))

    if is_active is not None and hasattr(Question, "is_active"):
        query = query.filter(Question.is_active == is_active)

    sort_columns = {
        "id": Question.id,
    }

    if hasattr(Question, "text"):
        sort_columns["text"] = Question.text

    if hasattr(Question, "quiz_id"):
        sort_columns["quiz_id"] = Question.quiz_id

    sort_column = sort_columns.get(sort_by, Question.id)

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


def get_question_by_id(
    db: Session,
    question_id: int,
):
    return db.query(Question).filter(Question.id == question_id).first()


def create_question(
    db: Session,
    question: QuestionCreate,
):
    db_question = Question(**question.model_dump())

    db.add(db_question)
    db.commit()
    db.refresh(db_question)

    return db_question


def update_question(
    db: Session,
    question_id: int,
    question: QuestionUpdate,
):
    db_question = get_question_by_id(
        db,
        question_id,
    )

    if not db_question:
        return None

    update_data = question.model_dump(exclude_unset=True)

    for key, value in update_data.items():
        setattr(db_question, key, value)

    db.commit()
    db.refresh(db_question)

    return db_question


def delete_question(
    db: Session,
    question_id: int,
):
    db_question = get_question_by_id(
        db,
        question_id,
    )

    if not db_question:
        return None

    db.delete(db_question)
    db.commit()

    return db_question


def get_answer_option_by_id(
    db: Session,
    answer_option_id: int,
):
    return (
        db.query(AnswerOption)
        .filter(AnswerOption.id == answer_option_id)
        .first()
    )


def get_correct_answer(
    db: Session,
    question_id: int,
):
    return (
        db.query(AnswerOption)
        .filter(
            AnswerOption.question_id == question_id,
            AnswerOption.is_correct.is_(True),
        )
        .first()
    )