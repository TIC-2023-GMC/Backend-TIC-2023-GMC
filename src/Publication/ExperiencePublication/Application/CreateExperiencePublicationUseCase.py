import inject
from src.Publication.ExperiencePublication.Domain.ExperiencePublication import (
    ExperiencePublication,
)
from src.Publication.Domain.PublicationRepository import PublicationRepository
from src.Publication.ExperiencePublication.Infrastructure.MongoDBExperiencePublicationRepository import (
    MongoDBExperiencePublicationRepository,
)


class CreateExperiencePublicationUseCase:
    @inject.params(publication_repository=MongoDBExperiencePublicationRepository)
    def __init__(self, publication_repository: PublicationRepository):
        self.publication_repository = publication_repository

    def execute(self, publication: ExperiencePublication) -> None:
        self.publication_repository.add_publication(publication=publication)
