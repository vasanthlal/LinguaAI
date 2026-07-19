from typing import List, Optional

from fastapi import APIRouter, Depends, Query
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


@router.get("/", response_model=List[LanguageResponse])
def get_languages(
    skip: int = Query(
        0,
        ge=0,
        description="Number of records to skip",
    ),
    limit: int = Query(
        10,
        ge=1,
        le=100,
        description="Maximum number of records to return",
    ),
    search: Optional[str] = Query(
        None,
        description="Search by language name",
    ),
    is_active: Optional[bool] = Query(
        None,
        description="Filter by active status",
    ),
    db: Session = Depends(get_db),
):
    return list_languages(
        db=db,
        skip=skip,
        limit=limit,
        search=search,
        is_active=is_active,
    )


@router.get("/{language_id}", response_model=LanguageResponse)
def get_language_by_id(
    language_id: int,
    db: Session = Depends(get_db),
):
    return get_language(
        db,
        language_id,
    )


@router.post("/", response_model=LanguageResponse, status_code=201)
def create_language(
    language: LanguageCreate,
    db: Session = Depends(get_db),
):
    return create_new_language(
        db,
        language,
    )


@router.put("/{language_id}", response_model=LanguageResponse)
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


@router.delete("/{language_id}")
def delete_language(
    language_id: int,
    db: Session = Depends(get_db),
):
    return delete_existing_language(
        db,
        language_id,
    )