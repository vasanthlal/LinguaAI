from pydantic import BaseModel


class QuestionAttemptBase(BaseModel):
    quiz_attempt_id: int
    question_id: int
    selected_answer_option_id: int


class QuestionAttemptCreate(QuestionAttemptBase):
    pass


class QuestionAttemptResponse(QuestionAttemptBase):
    id: int
    is_correct: bool
    points_awarded: int

    model_config = {"from_attributes": True}
