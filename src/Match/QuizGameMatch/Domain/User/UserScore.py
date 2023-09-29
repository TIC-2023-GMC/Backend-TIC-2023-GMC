from src.Photo.Domain.Photo import Photo
from src.Shared.Model import Model


class UserScore(Model):
    user_first_name: str
    user_last_name: str
    user_photo: Photo
    match_game_score: int
    match_game_time: int
