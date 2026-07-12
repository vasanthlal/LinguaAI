from pydantic import BaseModel


class AnswerOptionBase(BaseModel):
    question_id: int
    option_text: str
    is_correct: bool = False
    display_order: int


class AnswerOptionCreate(AnswerOptionBase):
    pass


class AnswerOptionUpdate(BaseModel):
    option_text: str | None = None
    is_correct: bool | None = None
    display_order: int | None = None


class AnswerOptionResponse(AnswerOptionBase):
    id: int

    model_config = {"from_attributes": True}
