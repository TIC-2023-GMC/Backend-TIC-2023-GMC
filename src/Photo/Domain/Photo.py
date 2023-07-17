from typing import Optional
from Shared.Model import Model


class Photo(Model):
    _id: Optional[int]
    img_path: str
