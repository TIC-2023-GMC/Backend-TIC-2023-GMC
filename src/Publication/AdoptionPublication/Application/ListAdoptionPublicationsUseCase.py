from typing import List
from Publication.AdoptionPublication.Domain.AdoptionPublication import (
    AdoptionPublication,
)
from Publication.Domain.PublicationRepository import PublicationRepository


class ListAdoptionPublicationsUseCase:
    def __init__(self, publication_repository: PublicationRepository):
        self.publication_repository = publication_repository

    def execute(self, pageNumber: int, pageSize: int) -> List[AdoptionPublication]:
        return self.publication_repository.get_all(
            pageNumber=pageNumber, pageSize=pageSize
        )
