from fastapi import APIRouter, Query
from src.Shared.Singleton import singleton
from src.Publication.ExperiencePublication.Application.CreateExperiencePublicationUseCase import (
    CreateExperiencePublicationUseCase,
)
from src.Publication.ExperiencePublication.Domain.ExperiencePublication import (
    ExperiencePublication,
)
from src.Publication.ExperiencePublication.Application.ListExperiencePublicationsUseCase import (
    ListExperiencePublicationsUseCase,
)
from typing import List, Tuple, Optional

router = APIRouter()


@singleton
class ExperienceFastAPIController:
    def __init__(self):
        self.list_experience = ListExperiencePublicationsUseCase()
        self.create_adoption = CreateExperiencePublicationUseCase()

    def create_experience_endpoint(self, publication: ExperiencePublication):
        self.create_adoption.execute(publication)

    def list_experiences_endpoint(
        self, species: str, date: str, page_number: int, page_size: int
    ):
        return self.list_experience.execute(
            species=species,
            experience_date=date,
            page_number=page_number,
            page_size=page_size,
        )


def get_experience_controller():
    return ExperienceFastAPIController()


@router.post("/add", status_code=201)
def create_adoption_endpoint(new_publication: ExperiencePublication):
    get_experience_controller().create_experience_endpoint(new_publication)


@router.get("/list", status_code=200)
def list_experiences_endpoint(
    species: Optional[str] = Query(None),
    date: Optional[str] = Query(None),
    page_number: int = Query(...),
    page_size: int = Query(...),
) -> Tuple[List[ExperiencePublication], int]:
    return get_experience_controller().list_experiences_endpoint(
        species, date, page_number, page_size
    )
