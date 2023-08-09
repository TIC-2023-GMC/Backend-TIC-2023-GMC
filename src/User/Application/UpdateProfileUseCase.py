import inject
from src.User.Domain.User import User

from src.User.Domain.UserRepository import UserRepository


class UpdateProfileUseCase:
    @inject.autoparams()
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def execute(self, updatedUser: User) -> None:
        self.user_repository.update_user(updatedUser)