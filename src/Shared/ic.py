import inject

from src.Publication.AdoptionPublication.Infrastructure.MongoDBAdoptionPublicationRepository import (
    MongoDBAdoptionPublicationRepository,
)
from src.Publication.Domain.PublicationRepository import PublicationRepository


def configure_ic() -> None:
    def configure(binder: inject.Binder) -> None:
        binder.bind(
            PublicationRepository,
            MongoDBAdoptionPublicationRepository(),
        )

    inject.configure_once(configure)
