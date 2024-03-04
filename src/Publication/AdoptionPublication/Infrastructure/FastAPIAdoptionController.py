from datetime import datetime
from typing import Annotated, List, Optional, Tuple

from fastapi import APIRouter, Depends, HTTPException, Query

from src.Publication.AdoptionPublication.Application.CreateAdoptionPublicationUseCase import (
    CreateAdoptionPublicationUseCase,
)
from src.Publication.AdoptionPublication.Application.ListAdoptionPublicationsUseCase import (
    ListAdoptionPublicationsUseCase,
)
from src.Publication.AdoptionPublication.Domain.AdoptionPublication import (
    AdoptionPublication,
)
from src.Shared.Singleton import singleton
from src.User.Domain.User import User
from src.User.Infrastructure.FastAPIUserController import get_current_active_user

router = APIRouter()


@singleton
class FastAPIAdoptionController:
    def __init__(self):
        self.create_adoption = CreateAdoptionPublicationUseCase()
        self.list_adoptions = ListAdoptionPublicationsUseCase()

    def create_adoption_endpoint(self, publication: AdoptionPublication) -> None:
        self.create_adoption.execute(publication)

    def list_adoptions_endpoint(
        self,
        species: str,
        date: datetime,
        location: str,
        page_number: int,
        page_size: int,
        user_id: str,
    ) -> Tuple[List[AdoptionPublication], int]:
        return self.list_adoptions.execute(
            species, date, location, page_number, page_size, user_id=user_id
        )


def get_adoption_controller() -> FastAPIAdoptionController:
    return FastAPIAdoptionController()


@router.post("/add", status_code=201)
def create_adoption_endpoint(new_publication: AdoptionPublication) -> None:
    try:
        get_adoption_controller().create_adoption_endpoint(new_publication)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/list", status_code=200)
def list_adoptions_endpoint(
    user: Annotated[User, Depends(get_current_active_user)],
    species: Optional[str] = Query(None),
    date: Optional[datetime] = Query(None),
    location: Optional[str] = Query(None),
    page_number: int = Query(...),
    page_size: int = Query(...),
) -> Tuple[List[AdoptionPublication], int]:
    try:
        return get_adoption_controller().list_adoptions_endpoint(
            species, date, location, page_number, page_size, user_id=user.id
        )
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
