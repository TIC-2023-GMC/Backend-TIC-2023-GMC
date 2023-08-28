from src.Interaction.Domain.InteractionFactory import InteractionFactory
from src.Interaction.Like.Domain.Like import Like
from src.User.Domain.User import User


class LikeFactory(InteractionFactory):
    @staticmethod
    def create(_id: int, user_id: str) -> Like:
        return Like(
            _id=_id,
            user_id=user_id
        )
