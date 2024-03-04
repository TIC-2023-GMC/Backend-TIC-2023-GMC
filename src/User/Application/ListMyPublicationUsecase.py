from typing import List, Tuple

import inject

from src.Publication.AdoptionPublication.Domain.AdoptionPublication import (
    AdoptionPublication,
)
from src.User.Domain.UserRepository import UserRepository


class ListMyPublicationsUseCase:
    @inject.autoparams()
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def execute(
        self,
        page_number: int,
        page_size: int,
        user_id: str,
    ) -> Tuple[List[AdoptionPublication], int]:
        response = self.user_repository.list_my_publications(
            page_number=page_number,
            page_size=page_size,
            user_id=user_id,
        )

        publications = response[0]
        user_favorites = self.user_repository.list_favorite_publications(
            page_number=page_number, page_size=page_size, user_id=user_id
        )
        user_favorite_ids = set(favorite.id for favorite in user_favorites[0])
        for publication in publications:
            publication.is_favorite = publication.id in user_favorite_ids
        return response
