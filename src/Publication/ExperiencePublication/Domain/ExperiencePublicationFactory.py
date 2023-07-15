from datetime import date
from Photo.Domain import Photo
from Publication.ExperiencePublication.Domain.ExperiencePublication import (
    ExperiencePublication,
)
from Publication.Domain.PublicationFactory import PublicationFactory
from User.Domain import User
from Interaction.Comment.Domain.Comment import Comment
from Interaction.Like.Domain.Like import Like


class ExperiencePublicationFactory(PublicationFactory):
    def createPublication(
        self,
        publication_id: int,
        user: User,
        description: str,
        publication_date: date,
        photo: Photo,
        likes: list[Like],
        comments: list[Comment],
        species: str,
    ) -> ExperiencePublication:
        return ExperiencePublication(
            publication_id=publication_id,
            user=user,
            description=description,
            publication_date=publication_date,
            photo=photo,
            likes=likes,
            comments=comments,
            species=species,
        )
