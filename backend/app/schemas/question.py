from pydantic import BaseModel, Field

from app.core.enums import QuestionType


class QuestionBase(BaseModel):
    quiz_id: int

    question_text: str = Field(
        min_length=5,
        max_length=1000,
        description="Question text",
    )

    question_type: QuestionType = Field(
        default=QuestionType.MCQ,
        description="Type of question",
    )

    difficulty: int = Field(
        default=1,
        ge=1,
        le=5,
        description="Difficulty level (1-5)",
    )

    points: int = Field(
        default=1,
        ge=1,
        le=100,
        description="Points awarded for this question",
    )

    explanation: str | None = Field(
        default=None,
        max_length=2000,
        description="Explanation shown after answering",
    )

    hint: str | None = Field(
        default=None,
        max_length=500,
        description="Hint shown before answering",
    )


class QuestionCreate(QuestionBase):
    model_config = {
        "json_schema_extra": {
            "example": {
                "quiz_id": 1,
                "question_text": "What is the capital of France?",
                "question_type": "MCQ",
                "difficulty": 2,
                "points": 5,
                "explanation": "Paris is the capital city of France.",
                "hint": "Think about the Eiffel Tower.",
            }
        }
    }


class QuestionUpdate(BaseModel):
    question_text: str | None = Field(
        default=None,
        min_length=5,
        max_length=1000,
    )

    question_type: QuestionType | None = None

    difficulty: int | None = Field(
        default=None,
        ge=1,
        le=5,
    )

    points: int | None = Field(
        default=None,
        ge=1,
        le=100,
    )

    explanation: str | None = Field(
        default=None,
        max_length=2000,
    )

    hint: str | None = Field(
        default=None,
        max_length=500,
    )


class QuestionResponse(QuestionBase):
    id: int

    model_config = {"from_attributes": True}
