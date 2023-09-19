from typing import List, Tuple

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from src.Publication.AdoptionPublication.Domain.AdoptionPublication import (
    AdoptionPublication,
)
from src.Shared.Singleton import singleton
from src.User.Application.AddFavoritePublicationUseCase import (
    AddFavoritePublicationUseCase,
)
from src.User.Application.GetUserByIdUseCase import GetUserByIdUseCase
from src.User.Application.ListFavoritePublicationsUseCase import (
    ListFavoritePublicationsUseCase,
)
from src.User.Application.ListMyPublicationUsecase import ListMyPublicationsUseCase
from src.User.Application.RemoveFavoritePublicationUseCase import (
    RemoveFavoritePublicationUseCase,
)
from src.User.Application.UpdateProfileUseCase import UpdateProfileUseCase
from src.User.Domain.User import User

router = APIRouter()


class FavoriteAdoptionData(BaseModel):
    pub_id: str
    user_id: str


@singleton
class FastAPIUserController:
    def __init__(self):
        self.user_list_favorites = ListFavoritePublicationsUseCase()
        self.user_add_favorite = AddFavoritePublicationUseCase()
        self.user_remove_favorite = RemoveFavoritePublicationUseCase()
        self.user_update_profile = UpdateProfileUseCase()
        self.user_list_my_publications = ListMyPublicationsUseCase()
        self.user_get_by_id = GetUserByIdUseCase()

    def add_favorite_adoption(self, pub_id: str, user_id: str) -> None:
        self.user_add_favorite.execute(pub_id=pub_id, user_id=user_id)

    def remove_favorite_adoption(self, pub_id: str, user_id: str) -> None:
        self.user_remove_favorite.execute(pub_id=pub_id, user_id=user_id)

    def update_user(self, updated_user: User) -> None:
        self.user_update_profile.execute(updated_user)

    def list_favorite_publication(
        self,
        user_id: str,
        page_number: int,
        page_size: int,
    ) -> Tuple[List[AdoptionPublication], int]:
        return self.user_list_favorites.execute(
            user_id=user_id,
            page_number=page_number,
            page_size=page_size,
        )

    def list_my_publications(
        self, page_number: int, page_size: int, user_id: str
    ) -> Tuple[List[AdoptionPublication], int]:
        return self.user_list_my_publications.execute(
            page_number=page_number,
            page_size=page_size,
            user_id=user_id,
        )

    def get_by_id(self, _id: str) -> User:
        return self.user_get_by_id.execute(_id=_id)


def get_user_controller() -> FastAPIUserController:
    return FastAPIUserController()


@router.get("/get_by_id", status_code=200)
def get_by_id_endpoint(_id: str) -> User:
    return get_user_controller().get_by_id(_id=_id)


@router.get("/list_favorite_adoptions", status_code=200)
def list_favorites_endpoint(
    user_id: str, page_number: int, page_size: int
) -> Tuple[List[AdoptionPublication], int]:
    return get_user_controller().list_favorite_publication(
        user_id=user_id,
        page_number=page_number,
        page_size=page_size,
    )


@router.put("/update_user", status_code=204)
def update_user_endpoint(updated_user: User) -> None:
    try:
        get_user_controller().update_user(updated_user)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.post("/add_favorite_adoption", status_code=201)
def add_favorite_adoption_endpoint(data: FavoriteAdoptionData) -> None:
    try:
        get_user_controller().add_favorite_adoption(
            pub_id=data.pub_id, user_id=data.user_id
        )
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.delete("/remove_favorite_adoption", status_code=204)
def remove_favorite_adoption_endpoint(data: FavoriteAdoptionData) -> None:
    try:
        get_user_controller().remove_favorite_adoption(
            pub_id=data.pub_id, user_id=data.user_id
        )
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/list_my_publications", status_code=200)
def list_my_publications_endpoint(
    page_number: int, page_size: int, user_id: str
) -> Tuple[List[AdoptionPublication], int]:
    return get_user_controller().list_my_publications(
        page_number=page_number,
        page_size=page_size,
        user_id=user_id,
    )
