from pydantic import BaseModel


class QuestionBase(BaseModel):
    quiz_id: int
    question_text: str
    question_type: str = "MCQ"
    difficulty: int = 1
    points: int = 1
    explanation: str | None = None
    hint: str | None = None


class QuestionCreate(QuestionBase):
    pass


class QuestionUpdate(BaseModel):
    question_text: str | None = None
    question_type: str | None = None
    difficulty: int | None = None
    points: int | None = None
    explanation: str | None = None
    hint: str | None = None


class QuestionResponse(QuestionBase):
    id: int

    model_config = {
        "from_attributes": True
    }