from datetime import datetime

from src.Interaction.Like.Domain.Like import Like
from src.Photo.Domain.Photo import Photo
from src.Publication.AdoptionPublication.Domain.AdoptionPublication import (
    AdoptionPublication,
)
from src.Publication.Domain.PublicationFactory import PublicationFactory
from src.User.Domain import User


class AdoptionPublicationFactory(PublicationFactory):
    @staticmethod
    def create_publication(
        _id: str,
        user: User,
        description: str,
        publication_date: datetime,
        photo: Photo,
        likes: list[Like],
        species: str,
        pet_size: str,
        pet_breed: str,
        pet_age: float,
        pet_sex: bool,
        pet_location: str,
        sterilized: bool,
        vaccination_card: bool,
        is_favorite: bool,
    ) -> AdoptionPublication:
        return AdoptionPublication(
            _id=_id,
            user=user,
            description=description,
            publication_date=publication_date,
            photo=photo,
            likes=likes,
            species=species,
            pet_size=pet_size,
            pet_breed=pet_breed,
            pet_age=pet_age,
            pet_sex=pet_sex,
            pet_location=pet_location,
            sterilized=sterilized,
            vaccination_card=vaccination_card,
            is_favorite=is_favorite,
        )
