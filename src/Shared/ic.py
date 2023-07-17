import inject
from src.Publication.Domain.PublicationRepository import PublicationRepository
from src.Publication.AdoptionPublication.Infrastructure.MongoDBAdoptionPublicationRepository import (
    MongoDBAdoptionPublicationRepository,
)


def configure(binder: inject.Binder) -> None:
    binder.bind(
        PublicationRepository,
        MongoDBAdoptionPublicationRepository(),
    )


inject.configure(configure)
