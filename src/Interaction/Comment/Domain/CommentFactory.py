from datetime import date
from src.Interaction.Comment.Domain.Comment import Comment
from src.Interaction.Domain.InteractionFactory import InteractionFactory
from src.User.Domain.User import User


class CommentFactory(InteractionFactory):
    @staticmethod
    def create(_id: str, comment_text: str, comment_date: date, user: User) -> Comment:
        return Comment(
            _id=_id,
            comment_text=comment_text,
            comment_date=comment_date,
            user=user,
        )
