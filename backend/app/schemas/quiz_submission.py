from pydantic import BaseModel, Field


class AnswerSubmission(BaseModel):
    question_id: int
    selected_answer_option_id: int


class QuizSubmission(BaseModel):
    user_id: int
    quiz_id: int

    answers: list[AnswerSubmission] = Field(
        min_length=1,
        description="User submitted answers",
    )


class QuestionResult(BaseModel):
    question_id: int
    selected_answer_option_id: int
    correct_answer_option_id: int

    is_correct: bool
    points_awarded: int

    explanation: str | None = None


class QuizResult(BaseModel):
    quiz_attempt_id: int

    score: int

    total_questions: int

    correct_answers: int

    incorrect_answers: int

    percentage: float

    passed: bool

    time_taken_seconds: int

    results: list[QuestionResult]
