from datetime import date
from Photo.Domain import Photo
from Publication.AdoptionPublication.Domain.AdoptionPublication import (
    AdoptionPublication,
)
from Publication.Domain.PublicationFactory import PublicationFactory
from User.Domain import User
from Interaction.Comment.Domain.Comment import Comment
from Interaction.Like.Domain.Like import Like


class AdoptionPublicationFactory(PublicationFactory):
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
        pet_size: str,
        pet_breed: str,
        pet_age: float,
        pet_sex: bool,
        pet_location: str,
        sterilized: bool,
        vaccination_card: bool,
    ) -> AdoptionPublication:
        return AdoptionPublication(
            publication_id=publication_id,
            user=user,
            description=description,
            publication_date=publication_date,
            photo=photo,
            likes=likes,
            comments=comments,
            species=species,
            pet_size=pet_size,
            pet_breed=pet_breed,
            pet_age=pet_age,
            pet_sex=pet_sex,
            pet_location=pet_location,
            sterilized=sterilized,
            vaccination_card=vaccination_card,
        )
