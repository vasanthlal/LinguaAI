from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.schemas.language import LanguageResponse
from app.services.language_service import (
    list_languages,
    get_language,
)

router = APIRouter(
    prefix="/languages",
    tags=["Languages"],
)


@router.get(
    "/",
    response_model=list[LanguageResponse],
)
def get_languages(
    db: Session = Depends(get_db),
):
    return list_languages(db)


@router.get(
    "/{language_id}",
    response_model=LanguageResponse,
)
def get_language_by_id(
    language_id: int,
    db: Session = Depends(get_db),
):
    return get_language(
        db,
        language_id,
    )
