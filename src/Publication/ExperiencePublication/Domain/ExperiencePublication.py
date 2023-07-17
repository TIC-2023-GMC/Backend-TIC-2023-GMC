from Publication.Domain.Publication import Publication
from User.Domain.User import User
from datetime import date
from Photo.Domain.Photo import Photo


class ExperiencePublication(Publication):
    def __init__(
        self,
        publication_id: str,
        user: User,
        description: str,
        publication_date: date,
        photo: Photo,
        likes: list,
        comments: list,
        species: str,
    ):
        super().__init__(
            publication_id,
            user,
            description,
            publication_date,
            photo,
            likes,
            comments,
            species,
        )
