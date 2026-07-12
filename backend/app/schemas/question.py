from pydantic import BaseModel


class QuestionBase(BaseModel):
    quiz_id: int
    question_text: str
    difficulty: int = 1


class QuestionCreate(QuestionBase):
    pass


class QuestionUpdate(BaseModel):
    question_text: str | None = None
    difficulty: int | None = None


class QuestionResponse(QuestionBase):
    id: int

    model_config = {
        "from_attributes": True
    }