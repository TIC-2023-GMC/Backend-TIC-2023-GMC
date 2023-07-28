from typing import List
from fastapi import APIRouter, UploadFile, File
from src.Publication.AdoptionPublication.Domain.AdoptionPublicationFactory import (
    AdoptionPublicationFactory,
)
from src.Publication.AdoptionPublication.Domain.AdoptionPublication import (
    AdoptionPublication,
)
from src.Shared.Singleton import singleton
from src.User.Application.ListFavoritePublicationsUseCase import (
    ListFavoritePublicationsUseCase,
)

router = APIRouter()


@singleton
class UserFastAPIController:
    def __init__(self):
        self.user_list_favorites = ListFavoritePublicationsUseCase()

    def list_favorite_publication(
        self, favorite_adoption_publications: List[str]
    ) -> List[AdoptionPublication]:
        return self.user_list_favorites.execute(
            favorite_adoption_publications=favorite_adoption_publications
        )


# Dependency
def get_user_controller() -> UserFastAPIController:
    return UserFastAPIController()


@router.post("/list_favorite_adoptions", status_code=200)
def list_favorites_endpoint(
    favorite_adoption_publications: List[str],
) -> List[AdoptionPublication]:
    return get_user_controller().list_favorite_publication(
        favorite_adoption_publications=favorite_adoption_publications
    )
