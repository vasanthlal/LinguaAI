from sqlalchemy.orm import Session

from app.models.quiz import Quiz
from app.schemas.quiz import QuizCreate, QuizUpdate


def get_all_quizzes(db: Session):
    return db.query(Quiz).all()


def get_quiz_by_id(db: Session, quiz_id: int):
    return db.query(Quiz).filter(Quiz.id == quiz_id).first()


def create_quiz(db: Session, quiz: QuizCreate):
    db_quiz = Quiz(**quiz.model_dump())

    db.add(db_quiz)
    db.commit()
    db.refresh(db_quiz)

    return db_quiz


def update_quiz(db: Session, quiz_id: int, quiz: QuizUpdate):
    db_quiz = get_quiz_by_id(db, quiz_id)

    if not db_quiz:
        return None

    update_data = quiz.model_dump(exclude_unset=True)

    for key, value in update_data.items():
        setattr(db_quiz, key, value)

    db.commit()
    db.refresh(db_quiz)

    return db_quiz


def delete_quiz(db: Session, quiz_id: int):
    db_quiz = get_quiz_by_id(db, quiz_id)

    if not db_quiz:
        return None

    db.delete(db_quiz)
    db.commit()

    return db_quiz
