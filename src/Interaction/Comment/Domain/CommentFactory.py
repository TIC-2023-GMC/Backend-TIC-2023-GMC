from datetime import date
from Interaction.Comment.Domain.Comment import Comment
from Interaction.Domain.InteractionFactory import InteractionFactory
from User.Domain.User import User


class CommentFactory(InteractionFactory):
    @staticmethod
    def create(
        comment_id: int, comment_text: str, comment_date: date, user: User
    ) -> Comment:
        return Comment(
            comment_id=comment_id,
            comment_text=comment_text,
            comment_date=comment_date,
            user=user,
        )
