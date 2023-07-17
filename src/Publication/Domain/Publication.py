from abc import ABC
from datetime import date
from Interaction.Comment.Domain.Comment import Comment
from Interaction.Like.Domain.Like import Like
from Photo.Domain.Photo import Photo
from Shared.Model import Model
from User.Domain.User import User
from typing import List, Optional


class Publication(Model, ABC):
    _id: Optional[int]
    user: User
    description: str
    publication_date: str
    photo: Photo
    likes: List[Like]
    comments: List[Comment]
    species: str
