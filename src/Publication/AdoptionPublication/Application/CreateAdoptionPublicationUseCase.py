from Publication.AdoptionPublication.Domain.AdoptionPublication import (
    AdoptionPublication,
)
from Publication.Domain.PublicationRepository import PublicationRepository


class CreateAdoptionPublicationUseCase:
    def __init__(self, publication_repository: PublicationRepository):
        self.publication_repository = publication_repository

    def execute(self, publication: AdoptionPublication):
        self.publication_repository.add_publication(publication=publication)
