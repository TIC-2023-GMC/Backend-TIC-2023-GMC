import inject
from src.Interaction.Like.Domain.LikeRepository import LikeRepository


class RemoveLikeUseCase:
    @inject.autoparams()
    def __init__(self, like_repository: LikeRepository):
        self.like_repository = like_repository

    def execute(self, user_id, pub_id, is_adoption) -> None:
        self.like_repository.remove_like(
            user_id=user_id, pub_id=pub_id, is_adoption=is_adoption
        )
