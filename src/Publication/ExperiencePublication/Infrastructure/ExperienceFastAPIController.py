from fastapi import APIRouter, Query
from src.Publication.ExperiencePublication.Domain.ExperiencePublication import (
    ExperiencePublication,
)
from src.Publication.ExperiencePublication.Application.ListExperiencePublicationsUseCase import (
    ListExperiencePublicationsUseCase,
)
from typing import List, Tuple, Optional

router = APIRouter()


class ExperienceFastAPIController:
    def __init__(self):
        self.list_experience = ListExperiencePublicationsUseCase()

    def create_experience_endpoint(self, publication: ExperiencePublication):
        pass

    def list_experiences_endpoint(
        self, species: str, date: str, page_number: int, page_size: int
    ):
        return self.list_experience.execute(species=species, experience_date=date, page_number=page_number, page_size=page_size)
# Dependency
def get_adoption_controller():
    return ExperienceFastAPIController()

@router.get("/experiences", status_code=200)
def list_experiences_endpoint(
    species: Optional[str] = Query(None),
    date: Optional[str] = Query(None),
    page_number: int = Query(...),
    page_size: int = Query(...),
) -> Tuple[List[ExperiencePublication], int]:
    return get_adoption_controller().list_experiences_endpoint(
        species, date, page_number, page_size
    )
