from datetime import datetime

from src.Interaction.Like.Domain.Like import Like
from src.Photo.Domain import Photo
from src.Publication.Domain.PublicationFactory import PublicationFactory
from src.Publication.ExperiencePublication.Domain.ExperiencePublication import (
    ExperiencePublication,
)
from src.User.Domain import User


class ExperiencePublicationFactory(PublicationFactory):
    @staticmethod
    def create_publication(
        _id: int,
        user: User,
        description: str,
        publication_date: datetime,
        photo: Photo,
        likes: list[Like],
        species: str,
    ) -> ExperiencePublication:
        return ExperiencePublication(
            _id=_id,
            user=user,
            description=description,
            publication_date=publication_date,
            photo=photo,
            likes=likes,
            species=species,
        )
