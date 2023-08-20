from typing import Optional
from src.Photo.Domain.Photo import Photo
from src.Shared.Model import Model


class GameInfo(Model):
    _id: Optional[str]
    game_name: str
    game_description: str
    game_image: Photo
