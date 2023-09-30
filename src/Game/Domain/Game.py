from typing import Optional

from src.Photo.Domain.Photo import Photo
from src.Shared.Model import Model


class Game(Model):
    _id: Optional[str]
    game_name: str
    game_category: str
    game_description: str
    game_image: Photo
