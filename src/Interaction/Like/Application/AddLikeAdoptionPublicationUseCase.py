
import inject
from src.Interaction.Like.Domain.LikeRepository import LikeRepository

class AddLikeAdoptionPublicationUseCase:
    @inject.autoparams()
    def __init__(self, like_repository: LikeRepository):
        self.like_repository = like_repository

    def execute(self, pub_id, user_id) -> None:
        self.like_repository.add_like_adoption_pub(pub_id=pub_id, user_id=user_id)