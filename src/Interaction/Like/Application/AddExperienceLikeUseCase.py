import inject

from src.Publication.Domain.PublicationRepository import PublicationRepository
from src.Publication.ExperiencePublication.Infrastructure.MongoDBExperiencePublicationRepository import (
    MongoDBExperiencePublicationRepository,
)


class AddExperienceLikeUseCase:
    @inject.params(publication_repository=MongoDBExperiencePublicationRepository)
    def __init__(self, publication_repository: PublicationRepository):
        self.publication_repository = publication_repository

    def execute(self, pub_id: str, user_id: str) -> None:
        self.publication_repository.add_like(pub_id=pub_id, user_id=user_id)
