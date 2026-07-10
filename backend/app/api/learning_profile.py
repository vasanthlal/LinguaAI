from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.schemas.learning_profile import (
    LearningProfileCreate,
    LearningProfileResponse,
)
from app.services.learning_profile_service import (
    save_learning_profile,
)

router = APIRouter(
    prefix="/learning-profile",
    tags=["Learning Profile"],
)


@router.post(
    "/{user_id}",
    response_model=LearningProfileResponse,
)
def create_profile(
    user_id: int,
    profile: LearningProfileCreate,
    db: Session = Depends(get_db),
):
    try:
        return save_learning_profile(
            db,
            user_id,
            profile,
        )

    except Exception as e:
        raise HTTPException(
            status_code=400,
            detail=str(e),
        )