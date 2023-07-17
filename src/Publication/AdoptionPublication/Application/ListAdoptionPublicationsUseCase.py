import inject
from typing import List, Tuple

from src.Publication.AdoptionPublication.Domain.AdoptionPublication import (
    AdoptionPublication,
)
from src.Publication.Domain.PublicationRepository import PublicationRepository


class ListAdoptionPublicationsUseCase:
    @inject.autoparams()
    def __init__(self, publication_repository: PublicationRepository):
        self.publication_repository = publication_repository

    def execute(
        self, page_number: int, page_size: int
    ) -> Tuple[List[AdoptionPublication], int]:
        return self.publication_repository.get_all(
            page_number=page_number, page_size=page_size
        )
