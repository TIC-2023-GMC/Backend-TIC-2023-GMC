import inject

from src.User.Domain.AuthService import AuthService
from src.User.Domain.User import User
from src.User.Domain.UserRepository import UserRepository


class RegisterUserUseCase:
    @inject.autoparams()
    def __init__(self, user_repository: UserRepository, auth_service: AuthService):
        self.user_repository = user_repository
        self.auth_service = auth_service

    def execute(self, user: User):
        existing_user = self.user_repository.get_user(user.email)
        if existing_user:
            raise Exception("El usuario ya existe")
        user.password = self.get_password_hash(user.password)
        self.user_repository.add_user(user)
        access_token = self.auth_service.create_access_token({"sub": user.email})
        return {"user": user, "access_token": access_token}

    def get_password_hash(self, password: str):
        return self.auth_service.encrypt(password)

    def create_access_token(self, data: dict):
        return self.auth_service.create_access_token(
            data, self.auth_service.access_token_expire_minutes
        )
