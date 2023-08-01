from typing import Optional
from src.Photo.Domain.Photo import Photo
from src.Shared.Model import Model


class Game(Model):
    _id: Optional[str]
    user_id: str
    game_name: str
    game_description: str
    game_image: Photo
    game_category: str
    game_score: int
