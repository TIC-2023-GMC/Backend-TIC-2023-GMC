import inject
from src.Publication.AdoptionPublication.Domain.AdoptionPublication import (
    AdoptionPublication,
)
from src.User.Domain.UserRepository import UserRepository
from typing import List, Tuple


class ListFavoritePublicationsUseCase:
    @inject.autoparams()
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def execute(
        self,
        favorite_adoption_publications: List[str],
        page_number: int,
        page_size: int,
    ) -> Tuple[List[AdoptionPublication], int]:
        return self.user_repository.list_favorite_publications(
            favorite_adoption_publications=favorite_adoption_publications,
            page_number=page_number,
            page_size=page_size,
        )
