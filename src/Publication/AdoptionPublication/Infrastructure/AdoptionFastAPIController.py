from fastapi import APIRouter, Query

from src.Publication.AdoptionPublication.Application.CreateAdoptionPublicationUseCase import (
    CreateAdoptionPublicationUseCase,
)
from src.Publication.AdoptionPublication.Application.ListAdoptionPublicationsUseCase import (
    ListAdoptionPublicationsUseCase,
)
from src.Publication.AdoptionPublication.Domain.AdoptionPublication import (
    AdoptionPublication,
)
from typing import List, Tuple, Optional

router = APIRouter()


class AdoptionFastAPIController:
    def __init__(self):
        self.create_adoption = CreateAdoptionPublicationUseCase()
        self.list_adoptions = ListAdoptionPublicationsUseCase()

    def create_adoption_endpoint(self, publication: AdoptionPublication):
        self.create_adoption.execute(publication)

    def list_adoptions_endpoint(
        self, species: str, date: str, location: str, page_number: int, page_size: int
    ):
        return self.list_adoptions.execute(
            species, date, location, page_number, page_size
        )


# Dependency
def get_adoption_controller():
    return AdoptionFastAPIController()


@router.post("/adoption", status_code=201)
def create_adoption_endpoint(new_publication: AdoptionPublication):
    get_adoption_controller().create_adoption_endpoint(new_publication)


@router.get("/adoptions", status_code=200)
def list_adoptions_endpoint(
    species: Optional[str] = Query(None),
    date: Optional[str] = Query(None),
    location: Optional[str] = Query(None),
    page_number: int = Query(...),
    page_size: int = Query(...),
) -> Tuple[List[AdoptionPublication], int]:
    return get_adoption_controller().list_adoptions_endpoint(
        species, date, location, page_number, page_size
    )
