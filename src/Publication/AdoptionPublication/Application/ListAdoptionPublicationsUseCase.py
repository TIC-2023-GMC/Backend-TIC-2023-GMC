import inject
from typing import List, Tuple
from datetime import date
from src.Publication.AdoptionPublication.Infrastructure.MongoDBAdoptionPublicationRepository import (
    MongoDBAdoptionPublicationRepository,
)

from src.Publication.AdoptionPublication.Domain.AdoptionPublication import (
    AdoptionPublication,
)
from src.Publication.Domain.PublicationRepository import PublicationRepository


class ListAdoptionPublicationsUseCase:
    @inject.params(publication_repository=MongoDBAdoptionPublicationRepository)
    def __init__(self, publication_repository: PublicationRepository):
        self.publication_repository = publication_repository

    def execute(
        self, species: str, date: date, location: str, page_number: int, page_size: int
    ) -> Tuple[List[AdoptionPublication], int]:
        return self.publication_repository.get_all(
            species=species,
            date=date,
            location=location,
            page_number=page_number,
            page_size=page_size,
        )
