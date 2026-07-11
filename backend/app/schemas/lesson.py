from pydantic import BaseModel


class LessonBase(BaseModel):
    course_id: int
    title: str
    content: str
    order: int


class LessonCreate(LessonBase):
    pass


class LessonUpdate(BaseModel):
    title: str | None = None
    content: str | None = None
    order: int | None = None


class LessonResponse(LessonBase):
    id: int

    model_config = {"from_attributes": True}
