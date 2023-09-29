from datetime import datetime
from typing import List, Tuple

import inject

from src.Publication.AdoptionPublication.Domain.AdoptionPublication import (
    AdoptionPublication,
)
from src.Publication.AdoptionPublication.Infrastructure.MongoDBAdoptionPublicationRepository import (
    MongoDBAdoptionPublicationRepository,
)
from src.Publication.Domain.PublicationRepository import PublicationRepository
from src.User.Domain.UserRepository import UserRepository


class ListAdoptionPublicationsUseCase:
    user_repository = inject.attr(UserRepository)

    @inject.params(publication_repository=MongoDBAdoptionPublicationRepository)
    def __init__(self, publication_repository: PublicationRepository):
        self.publication_repository = publication_repository

    def execute(
        self,
        species: str,
        date: datetime,
        location: str,
        page_number: int,
        page_size: int,
        user_id: str,
    ) -> Tuple[List[AdoptionPublication], int]:
        response = self.publication_repository.get_all(
            species=species,
            date=date,
            location=location,
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
