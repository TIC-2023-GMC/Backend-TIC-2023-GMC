from datetime import datetime
from typing import Annotated, List, Optional, Tuple

from fastapi import APIRouter, Depends, HTTPException, Query

from src.Publication.ExperiencePublication.Application.CreateExperiencePublicationUseCase import (
    CreateExperiencePublicationUseCase,
)
from src.Publication.ExperiencePublication.Application.ListExperiencePublicationsUseCase import (
    ListExperiencePublicationsUseCase,
)
from src.Publication.ExperiencePublication.Domain.ExperiencePublication import (
    ExperiencePublication,
)
from src.Shared.Singleton import singleton
from src.User.Domain.User import User
from src.User.Infrastructure.FastAPIUserController import get_current_active_user

router = APIRouter()


@singleton
class FastAPIExperienceController:
    def __init__(self):
        self.list_experience = ListExperiencePublicationsUseCase()
        self.create_adoption = CreateExperiencePublicationUseCase()

    def create_experience_endpoint(self, publication: ExperiencePublication) -> None:
        self.create_adoption.execute(publication)

    def list_experiences_endpoint(
        self,
        species: str,
        date: datetime,
        page_number: int,
        page_size: int,
        user_id: str,
    ) -> Tuple[List[ExperiencePublication], int]:
        return self.list_experience.execute(
            species=species,
            experience_date=date,
            page_number=page_number,
            page_size=page_size,
            user_id=user_id,
        )


def get_experience_controller() -> FastAPIExperienceController:
    return FastAPIExperienceController()


@router.post("/add", status_code=201)
def create_experience_endpoint(new_publication: ExperiencePublication) -> None:
    try:
        get_experience_controller().create_experience_endpoint(new_publication)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/list", status_code=200)
def list_experiences_endpoint(
    user: Annotated[User, Depends(get_current_active_user)],
    species: Optional[str] = Query(None),
    date: Optional[datetime] = Query(None),
    page_number: int = Query(...),
    page_size: int = Query(...),
) -> Tuple[List[ExperiencePublication], int]:
    try:
        return get_experience_controller().list_experiences_endpoint(
            species, date, page_number, page_size, user.id
        )
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
