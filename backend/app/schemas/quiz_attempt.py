from datetime import datetime
from pydantic import BaseModel


class QuizAttemptBase(BaseModel):
    user_id: int
    quiz_id: int


class QuizAttemptCreate(QuizAttemptBase):
    pass


class QuizAttemptResponse(QuizAttemptBase):
    id: int
    score: int
    total_questions: int
    correct_answers: int
    status: str
    completed_at: datetime | None = None

    model_config = {"from_attributes": True}
