from pydantic import BaseModel, Field


class AnswerOptionBase(BaseModel):
    question_id: int = Field(
        ...,
        gt=0,
        description="Question ID",
    )

    option_text: str = Field(
        ...,
        min_length=1,
        max_length=255,
        description="Answer option text",
    )

    is_correct: bool = Field(
        default=False,
        description="Whether this option is the correct answer",
    )

    display_order: int = Field(
        ...,
        gt=0,
        description="Display order of the option",
    )


class AnswerOptionCreate(AnswerOptionBase):
    model_config = {
        "json_schema_extra": {
            "example": {
                "question_id": 1,
                "option_text": "Paris",
                "is_correct": True,
                "display_order": 1,
            }
        }
    }


class AnswerOptionUpdate(BaseModel):
    question_id: int | None = Field(
        default=None,
        gt=0,
    )

    option_text: str | None = Field(
        default=None,
        min_length=1,
        max_length=255,
    )

    is_correct: bool | None = None

    display_order: int | None = Field(
        default=None,
        gt=0,
    )


class AnswerOptionResponse(AnswerOptionBase):
    id: int

    model_config = {
        "from_attributes": True,
    }
