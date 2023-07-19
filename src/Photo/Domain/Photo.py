from typing import Optional
from src.Shared.Model import Model


class Photo(Model):
    _id: Optional[str]
    img_path: str
