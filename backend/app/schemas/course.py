from pydantic import BaseModel, Field


class CourseBase(BaseModel):
    language_id: int = Field(..., gt=0)
    title: str = Field(..., min_length=1, max_length=150)
    description: str | None = None
    level: str = Field(..., min_length=1, max_length=50)


class CourseCreate(CourseBase):
    pass


class CourseUpdate(BaseModel):
    language_id: int | None = Field(default=None, gt=0)
    title: str | None = Field(default=None, min_length=1, max_length=150)
    description: str | None = None
    level: str | None = Field(default=None, min_length=1, max_length=50)


class CourseResponse(CourseBase):
    id: int

    model_config = {
        "from_attributes": True,
    }
