from datetime import date
from typing import List
from Publication.AdoptionPublication.Domain.AdoptionPublication import (
    AdoptionPublication,
)
from Publication.Domain.PublicationRepository import PublicationRepository


class FilterListAdoptionPublicationUseCase:
    def __init__(self, publication_repository: PublicationRepository):
        self.publication_repository = publication_repository

    def execute(
        self, species: str, date: date, location: str, pageNumber: int, pageSize: int
    ) -> List[AdoptionPublication]:
        return self.publication_repository.get_by_filters(
            species=species,
            date=date,
            location=location,
            pageNumber=pageNumber,
            pageSize=pageSize,
        )
