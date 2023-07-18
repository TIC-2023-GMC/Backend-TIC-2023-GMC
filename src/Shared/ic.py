import inject

from src.Publication.AdoptionPublication.Infrastructure.MongoDBAdoptionPublicationRepository import (
    MongoDBAdoptionPublicationRepository,
)
from src.Publication.Domain.PublicationRepository import PublicationRepository

from src.Photo.Domain.PhotoRepository import PhotoRepository
from src.Photo.Infrastructure.FirebasePhotoRepository import FirebasePhotoRepository


def configure_ic() -> None:
    def configure(binder: inject.Binder) -> None:
        binder.bind(
            PublicationRepository,
            MongoDBAdoptionPublicationRepository(),
        )
        binder.bind(
            PhotoRepository,
            FirebasePhotoRepository(),
        )

    inject.configure_once(configure)
