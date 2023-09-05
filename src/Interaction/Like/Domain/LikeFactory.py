from src.Interaction.Domain.InteractionFactory import InteractionFactory
from src.Interaction.Like.Domain.Like import Like
from src.User.Domain.User import User


class LikeFactory(InteractionFactory):
    @staticmethod
    def create(user_id: str) -> Like:
        return Like(user_id=user_id)
