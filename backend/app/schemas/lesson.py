from pydantic import BaseModel, Field


class LessonBase(BaseModel):
    course_id: int = Field(..., gt=0)
    title: str = Field(..., min_length=1, max_length=150)
    content: str = Field(..., min_length=1)
    order: int = Field(..., gt=0)


class LessonCreate(LessonBase):
    pass


class LessonUpdate(BaseModel):
    course_id: int | None = Field(default=None, gt=0)
    title: str | None = Field(default=None, min_length=1, max_length=150)
    content: str | None = Field(default=None, min_length=1)
    order: int | None = Field(default=None, gt=0)


class LessonResponse(LessonBase):
    id: int

    model_config = {
        "from_attributes": True,
    }
