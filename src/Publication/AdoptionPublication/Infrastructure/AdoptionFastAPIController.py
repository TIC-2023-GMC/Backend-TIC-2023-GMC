from bson import ObjectId
from fastapi import APIRouter, Query, UploadFile, File
from src.Photo.Domain.Photo import Photo
from src.Photo.Domain.PhotoFactory import PhotoFactory
from src.Photo.Application.SavePhotoUseCase import SavePhotoUseCase
from typing import Annotated

from src.Publication.AdoptionPublication.Application.CreateAdoptionPublicationUseCase import (
    CreateAdoptionPublicationUseCase,
)
from src.Publication.AdoptionPublication.Application.ListAdoptionPublicationsUseCase import (
    ListAdoptionPublicationsUseCase,
)
from src.Publication.AdoptionPublication.Application.FilterListAdoptionPublicationUseCase import (
    FilterListAdoptionPublicationUseCase,
)
from src.Publication.AdoptionPublication.Domain.AdoptionPublication import (
    AdoptionPublication,
)
from typing import List, Tuple, Optional

router = APIRouter()


class AdoptionFastAPIController:
    def __init__(self):
        self.create_adoption = CreateAdoptionPublicationUseCase()
        self.save_photo = SavePhotoUseCase()
        self.list_adoptions = ListAdoptionPublicationsUseCase()
        self.filtered_list_adoptions = FilterListAdoptionPublicationUseCase()

    def create_adoption_endpoint(
        self, publication: AdoptionPublication, photo: UploadFile
    ):
        new_publication = self.save_photo.execute_pub(photo, publication)
        self.create_adoption.execute(new_publication)

    def list_adoptions_endpoint(self, page_number: int, page_size: int):
        return self.list_adoptions.execute(page_number, page_size)

    def list_filtered_adoptions_endpoint(
        self, species: str, date: str, location: str, page_number: int, page_size: int
    ):
        return self.filtered_list_adoptions.execute(
            species, date, location, page_number, page_size
        )


# Dependency
def get_adoption_controller():
    return AdoptionFastAPIController()


@router.post("/adoption", status_code=201)
def create_adoption_endpoint(new_publication: AdoptionPublication, photo: UploadFile = File(...) ):
    get_adoption_controller().create_adoption_endpoint(new_publication, photo)


@router.get("/adoptions", status_code=200)
def list_adoptions_endpoint(
    page_number: int, page_size: int
) -> Tuple[List[AdoptionPublication], int]:
    return get_adoption_controller().list_adoptions_endpoint(page_number, page_size)


@router.get("/adoptions/filtered", status_code=200)
def list_filtered_adoptions_endpoint(
    species: Optional[str] = Query(None),
    date: Optional[str] = Query(None),
    location: Optional[str] = Query(None),
    page_number: int = Query(...),
    page_size: int = Query(...),
):
    return get_adoption_controller().list_filtered_adoptions_endpoint(
        species, date, location, page_number, page_size
    )
