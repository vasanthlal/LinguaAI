from sqlalchemy.orm import Session

from app.repositories import question_repository
from app.schemas.question import QuestionCreate, QuestionUpdate


def get_questions(db: Session):
    return question_repository.get_all_questions(db)


def get_question(db: Session, question_id: int):
    return question_repository.get_question_by_id(db, question_id)


def create_question(db: Session, question: QuestionCreate):
    return question_repository.create_question(db, question)


def update_question(db: Session, question_id: int, question: QuestionUpdate):
    return question_repository.update_question(db, question_id, question)


def delete_question(db: Session, question_id: int):
    return question_repository.delete_question(db, question_id)
