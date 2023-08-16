import inject
from src.Publication.AdoptionPublication.Domain.AdoptionPublication import (
    AdoptionPublication,
)
from src.User.Domain.UserRepository import UserRepository
from typing import List, Tuple


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
        return self.user_repository.list_my_publications(
            page_number=page_number,
            page_size=page_size,
            user_id=user_id,
        )
