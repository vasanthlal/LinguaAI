from pydantic import BaseModel


class CourseBase(BaseModel):
    language_id: int
    title: str
    description: str | None = None
    level: str


class CourseCreate(CourseBase):
    pass


class CourseUpdate(BaseModel):
    title: str | None = None
    description: str | None = None
    level: str | None = None


class CourseResponse(CourseBase):
    id: int

    model_config = {"from_attributes": True}
