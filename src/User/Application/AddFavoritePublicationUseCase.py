import inject

from src.User.Domain.UserRepository import UserRepository


class AddFavoritePublicationUseCase:
    @inject.autoparams()
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def execute(self, pub_id: str, user_id: str) -> None:
        self.user_repository.add_favorite_pub(pub_id=pub_id, user_id=user_id)
