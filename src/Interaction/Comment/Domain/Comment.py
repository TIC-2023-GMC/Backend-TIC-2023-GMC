from datetime import datetime
from src.Photo.Domain.Photo import Photo
from src.Interaction.Domain.Interaction import Interaction


class Comment(Interaction):
    _id: str
    user_first_name: str
    user_last_name: str
    user_photo: Photo
    comment_text: str
    comment_date: datetime
