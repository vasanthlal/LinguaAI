from pydantic import BaseModel, Field


class QuizBase(BaseModel):
    lesson_id: int = Field(..., gt=0)
    title: str = Field(..., min_length=1, max_length=150)
    passing_score: int = Field(default=70, ge=0, le=100)


class QuizCreate(QuizBase):
    pass


class QuizUpdate(BaseModel):
    lesson_id: int | None = Field(default=None, gt=0)
    title: str | None = Field(default=None, min_length=1, max_length=150)
    passing_score: int | None = Field(default=None, ge=0, le=100)


class QuizResponse(QuizBase):
    id: int

    model_config = {
        "from_attributes": True,
    }
