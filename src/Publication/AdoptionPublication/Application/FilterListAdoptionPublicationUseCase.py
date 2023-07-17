from datetime import date
import inject
from typing import List

from src.Publication.AdoptionPublication.Domain.AdoptionPublication import (
    AdoptionPublication,
)
from src.Publication.Domain.PublicationRepository import PublicationRepository


class FilterListAdoptionPublicationUseCase:
    @inject.autoparams()
    def __init__(self, publication_repository: PublicationRepository):
        self.publication_repository = publication_repository

    def execute(
        self, species: str, date: date, location: str, pageNumber: int, pageSize: int
    ) -> List[AdoptionPublication]:
        return self.publication_repository.get_by_filters(
            species=species,
            date=date,
            location=location,
            page_number=pageNumber,
            page_size=pageSize,
        )
