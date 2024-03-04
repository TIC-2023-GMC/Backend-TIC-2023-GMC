from abc import ABC
from datetime import datetime
from typing import List, Optional, Tuple

from src.Interaction.Like.Domain.Like import Like
from src.Photo.Domain.Photo import Photo
from src.Shared.Model import Model
from src.User.Domain.User import User


class Publication(Model, ABC):
    _id: Optional[str]
    user: User
    description: str
    publication_date: datetime
    photo: Photo
    likes: List[Like] | Tuple[int, bool]
    species: str

    @property
    def id(self):
        return self._id
