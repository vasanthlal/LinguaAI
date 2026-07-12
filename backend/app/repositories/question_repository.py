from sqlalchemy.orm import Session

from app.models.question import Question
from app.schemas.question import QuestionCreate, QuestionUpdate
from app.models.answer_option import AnswerOption


def get_all_questions(db: Session):
    return db.query(Question).all()


def get_question_by_id(db: Session, question_id: int):
    return db.query(Question).filter(Question.id == question_id).first()


def create_question(db: Session, question: QuestionCreate):
    db_question = Question(**question.model_dump())

    db.add(db_question)
    db.commit()
    db.refresh(db_question)

    return db_question


def update_question(db: Session, question_id: int, question: QuestionUpdate):
    db_question = get_question_by_id(db, question_id)

    if not db_question:
        return None

    update_data = question.model_dump(exclude_unset=True)

    for key, value in update_data.items():
        setattr(db_question, key, value)

    db.commit()
    db.refresh(db_question)

    return db_question


def delete_question(db: Session, question_id: int):
    db_question = get_question_by_id(db, question_id)

    if not db_question:
        return None

    db.delete(db_question)
    db.commit()

    return db_question


def get_answer_option_by_id(
    db: Session,
    answer_option_id: int,
):
    return db.query(AnswerOption).filter(AnswerOption.id == answer_option_id).first()


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
