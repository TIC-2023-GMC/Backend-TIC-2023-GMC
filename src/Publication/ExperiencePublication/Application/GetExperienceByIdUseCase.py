import inject
from src.Publication.Domain.PublicationRepository import PublicationRepository
from src.Publication.ExperiencePublication.Domain.ExperiencePublication import (
    ExperiencePublication,
)
from src.Publication.ExperiencePublication.Infrastructure.MongoDBExperiencePublicationRepository import (
    MongoDBExperiencePublicationRepository,
)


class GetExperienceByIdUseCase:
    @inject.params(publication_repository=MongoDBExperiencePublicationRepository)
    def __init__(self, publication_repository: PublicationRepository):
        self.publication_repository = publication_repository

    def execute(
        self,
        pub_id: str,
    ) -> ExperiencePublication:
        return self.publication_repository.get_by_id(
            id=pub_id,
        )
