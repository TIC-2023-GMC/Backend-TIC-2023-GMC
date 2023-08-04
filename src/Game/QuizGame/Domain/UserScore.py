from typing import Optional
from src.Photo.Domain.Photo import Photo
from src.Shared.Model import Model


class UserScore(Model):
    user_first_name: str
    user_last_name: str
    user_photo: Photo
    game_score: int
    game_time: int
