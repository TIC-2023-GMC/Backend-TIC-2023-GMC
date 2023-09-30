import inject

from src.User.Domain.User import User
from src.User.Domain.UserRepository import UserRepository


class GetUserByIdUseCase:
    @inject.autoparams()
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def execute(self, _id: str) -> User:
        return self.user_repository.get_by_id(_id=_id)
