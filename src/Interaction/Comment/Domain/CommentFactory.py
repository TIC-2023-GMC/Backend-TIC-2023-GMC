from datetime import date

from src.Interaction.Comment.Domain.Comment import Comment
from src.Interaction.Domain.InteractionFactory import InteractionFactory
from src.Photo.Domain.Photo import Photo


class CommentFactory(InteractionFactory):
    @staticmethod
    def create(
        _id: str,
        user_first_name: str,
        user_last_name: str,
        comment_text: str,
        comment_date: date,
        user_photo: Photo,
        user_id: str,
    ) -> Comment:
        return Comment(
            _id=_id,
            user_first_name=user_first_name,
            user_last_name=user_last_name,
            user_photo=user_photo,
            comment_text=comment_text,
            comment_date=comment_date,
            user_id=user_id,
        )
