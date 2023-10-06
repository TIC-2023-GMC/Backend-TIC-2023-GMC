import inject

from src.User.Domain.User import User
from src.User.Domain.UserRepository import UserRepository


class UpdateProfileUseCase:
    @inject.autoparams()
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def execute(self, updated_user: User) -> None:
        existing_user: User = self.user_repository.get_user(
            updated_user.email, updated_user.mobile_phone
        )

        if existing_user and existing_user._id != updated_user._id:
            raise Exception("Ya existe un usuario con ese email o celular")

        self.user_repository.update_user(updated_user)
