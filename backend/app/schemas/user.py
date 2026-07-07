from pydantic import BaseModel, EmailStr


class UserCreate(BaseModel):
    full_name: str
    email: EmailStr
    password: str
    native_language: str
    target_language: str


class UserLogin(BaseModel):
    email: EmailStr
    password: str


class UserResponse(BaseModel):
    id: int
    full_name: str
    email: EmailStr
    native_language: str
    target_language: str
    is_active: bool

    model_config = {
        "from_attributes": True
    }