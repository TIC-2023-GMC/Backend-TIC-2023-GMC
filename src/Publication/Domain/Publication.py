from abc import ABC
from datetime import date
from Interaction.Comment.Domain.Comment import Comment
from Interaction.Like.Domain.Like import Like
from Photo.Domain.Photo import Photo
from Shared.Model import Model
from User.Domain.User import User
from typing import List


class Publication(Model, ABC):
    publication_id: int
    user: User
    description: str
    publication_date: date
    photo: Photo
    likes: List[Like]
    comments: List[Comment]
    species: str
