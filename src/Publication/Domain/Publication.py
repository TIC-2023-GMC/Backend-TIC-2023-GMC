from abc import ABC
from datetime import date
from typing import List, Optional
from src.Interaction.Comment.Domain.Comment import Comment
from src.Interaction.Like.Domain.Like import Like
from src.Photo.Domain.Photo import Photo
from src.Shared.Model import Model
from src.User.Domain.User import User


class Publication(Model, ABC):
    _id: Optional[str]
    user: User
    description: str
    publication_date: str
    photo: Optional[Photo]
    likes: List[Like]
    comments: List[Comment]
    species: str
