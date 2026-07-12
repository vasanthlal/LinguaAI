from pydantic import BaseModel


class QuizBase(BaseModel):
    lesson_id: int
    title: str
    passing_score: int = 70


class QuizCreate(QuizBase):
    pass


class QuizUpdate(BaseModel):
    title: str | None = None
    passing_score: int | None = None


class QuizResponse(QuizBase):
    id: int

    model_config = {
        "from_attributes": True
    }