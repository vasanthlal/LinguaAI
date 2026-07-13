from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.schemas.language import (
    LanguageCreate,
    LanguageResponse,
    LanguageUpdate,
)
from app.services.language_service import (
    create_new_language,
    delete_existing_language,
    get_language,
    list_languages,
    update_existing_language,
)

router = APIRouter(
    prefix="/languages",
    tags=["Languages"],
)


@router.post(
    "/",
    response_model=LanguageResponse,
    status_code=201,
)
def create_language(
    language: LanguageCreate,
    db: Session = Depends(get_db),
):
    return create_new_language(
        db,
        language,
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


@router.put(
    "/{language_id}",
    response_model=LanguageResponse,
)
def update_language(
    language_id: int,
    language: LanguageUpdate,
    db: Session = Depends(get_db),
):
    return update_existing_language(
        db,
        language_id,
        language,
    )


@router.delete(
    "/{language_id}",
)
def delete_language(
    language_id: int,
    db: Session = Depends(get_db),
):
    return delete_existing_language(
        db,
        language_id,
    )
