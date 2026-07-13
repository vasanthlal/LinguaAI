from pydantic import BaseModel, Field


class LanguageBase(BaseModel):
    name: str = Field(..., max_length=100)
    code: str = Field(..., max_length=10)
    native_name: str = Field(..., max_length=100)
    country_code: str = Field(..., max_length=10)
    is_active: bool = True


class LanguageCreate(LanguageBase):
    pass


class LanguageUpdate(LanguageBase):
    pass


class LanguageResponse(LanguageBase):
    id: int

    model_config = {
        "from_attributes": True,
    }
