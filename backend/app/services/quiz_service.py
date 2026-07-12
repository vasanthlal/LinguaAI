from sqlalchemy.orm import Session

from app.repositories import quiz_repository
from app.schemas.quiz import QuizCreate, QuizUpdate


def get_quizzes(db: Session):
    return quiz_repository.get_all_quizzes(db)


def get_quiz(db: Session, quiz_id: int):
    return quiz_repository.get_quiz_by_id(db, quiz_id)


def create_quiz(db: Session, quiz: QuizCreate):
    return quiz_repository.create_quiz(db, quiz)


def update_quiz(db: Session, quiz_id: int, quiz: QuizUpdate):
    return quiz_repository.update_quiz(db, quiz_id, quiz)


def delete_quiz(db: Session, quiz_id: int):
    return quiz_repository.delete_quiz(db, quiz_id)