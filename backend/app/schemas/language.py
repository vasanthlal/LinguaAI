from pydantic import BaseModel


class LanguageResponse(BaseModel):
    id: int
    name: str
    code: str
    native_name: str
    country_code: str
    is_active: bool

    model_config = {"from_attributes": True}
