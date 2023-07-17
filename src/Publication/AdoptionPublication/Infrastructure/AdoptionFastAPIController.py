from fastapi import FastAPI, APIRouter

from Publication.AdoptionPublication.Application.CreateAdoptionPublicationUseCase import (
    CreateAdoptionPublicationUseCase,
)
from Publication.AdoptionPublication.Application.ListAdoptionPublicationsUseCase import (
    ListAdoptionPublicationsUseCase,
)
from Publication.AdoptionPublication.Application.FilterListAdoptionPublicationUseCase import (
    FilterListAdoptionPublicationUseCase,
)
from Publication.AdoptionPublication.Domain.AdoptionPublication import (
    AdoptionPublication,
)

router = APIRouter()


class AdoptionFastAPIController:
    def __init__(
        self,
        create_adoption: CreateAdoptionPublicationUseCase,
        list_adoptions: ListAdoptionPublicationsUseCase,
        filtered_list_adoptions: FilterListAdoptionPublicationUseCase,
    ):
        self.create_adoption = create_adoption
        self.list_adoptions = list_adoptions
        self.filtered_list_adoptions = filtered_list_adoptions

    def create_adoption_endpoint(self, publication: AdoptionPublication):
        self.create_adoption.execute(publication)

    def list_adoptions_endpoint(self, pageNumber: int, pageSize: int):
        self.list_adoptions.execute(pageNumber, pageSize)

    def list_filtered_adoptions_endpoint(
        self, species: str, date: str, location: str, pageNumber: int, pageSize: int
    ):
        self.filtered_list_adoptions.execute(
            species, date, location, pageNumber, pageSize
        )


# Dependency
def get_adoption_controller():
    return AdoptionFastAPIController(
        CreateAdoptionPublicationUseCase(),
        ListAdoptionPublicationsUseCase(),
        FilterListAdoptionPublicationUseCase(),
    )


@router.post("/adoption", status_code=201)
def create_adoption_endpoint(newPublication: AdoptionPublication):
    get_adoption_controller().create_adoption_endpoint(newPublication)


@router.get("/adoptions", status_code=200)
def list_adoptions_endpoint(pageNumber: int, pageSize: int):
    get_adoption_controller().list_adoptions_endpoint(pageNumber, pageSize)


@router.get("/adoptions/filtered", status_code=200)
def list_filtered_adoptions_endpoint(
    species: str, date: str, location: str, pageNumber: int, pageSize: int
):
    get_adoption_controller().list_filtered_adoptions_endpoint(
        species, date, location, pageNumber, pageSize
    )
