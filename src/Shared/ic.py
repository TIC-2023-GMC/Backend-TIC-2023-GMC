import inject
from src.Parish.Infrastructure.MongoDBParishRepository import MongoDBParishRepository
from src.Parish.Domain.ParishRepository import ParishRepository
from src.Publication.Domain.PublicationRepository import PublicationRepository
from src.Photo.Domain.PhotoRepository import PhotoRepository
from src.Photo.Infrastructure.FirebasePhotoRepository import FirebasePhotoRepository

PublicationRepoAlias = PublicationRepository
def configure_ic() -> None:
    def configure(binder: inject.Binder) -> None:
        binder.bind(
            PhotoRepository,
            FirebasePhotoRepository(),
        )
        binder.bind(
            ParishRepository,
            MongoDBParishRepository(),
        )

    inject.configure_once(configure)
