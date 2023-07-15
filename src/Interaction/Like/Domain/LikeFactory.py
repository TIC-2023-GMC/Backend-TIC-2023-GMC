from Interaction.Domain.InteractionFactory import InteractionFactory
from Interaction.Like.Domain.Like import Like
from User.Domain.User import User


class LikeFactory(InteractionFactory):
    @staticmethod
    def create(like_id: int, user: User) -> Like:
        return Like(
            like_id=like_id,
            user=user,
        )
