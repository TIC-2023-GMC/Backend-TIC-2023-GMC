import inject
from typing import List, Tuple
from src.Publication.AdoptionPublication.Infrastructure.MongoDBAdoptionPublicationRepository import (
    MongoDBAdoptionPublicationRepository,
)

from src.Publication.AdoptionPublication.Domain.AdoptionPublication import (
    AdoptionPublication,
)
from src.Publication.Domain.PublicationRepository import PublicationRepository


class GetAdoptionByIdUseCase:
    @inject.params(publication_repository=MongoDBAdoptionPublicationRepository)
    def __init__(self, publication_repository: PublicationRepository):
        self.publication_repository = publication_repository

    def execute(
        self,
        pub_id: int,
    ) -> Tuple[List[AdoptionPublication], int]:
        return self.publication_repository.get_by_id(
            id=pub_id,
        )
