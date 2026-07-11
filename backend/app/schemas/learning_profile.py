from pydantic import BaseModel


class LearningProfileCreate(BaseModel):
    native_language: str
    target_language: str
    current_level: str
    daily_goal_minutes: int
    learning_goal: str


class LearningProfileResponse(BaseModel):
    id: int
    user_id: int
    native_language: str
    target_language: str
    current_level: str
    daily_goal_minutes: int
    learning_goal: str

    model_config = {"from_attributes": True}
