import inject

from src.Publication.AdoptionPublication.Infrastructure.MongoDBAdoptionPublicationRepository import (
    MongoDBAdoptionPublicationRepository,
)
from src.Publication.Domain.PublicationRepository import PublicationRepository


class RemoveAdoptionLikeUseCase:
    @inject.params(publication_repository=MongoDBAdoptionPublicationRepository)
    def __init__(self, publication_repository: PublicationRepository):
        self.publication_repository = publication_repository

    def execute(self, pub_id: str, user_id: str) -> None:
        self.publication_repository.remove_like(pub_id=pub_id, user_id=user_id)
