from datetime import timedelta

import inject

from src.User.Domain.AuthService import AuthService
from src.User.Domain.User import User
from src.User.Domain.UserFactory import UserFactory
from src.User.Domain.UserRepository import UserRepository


class LoginUseCase:
    @inject.autoparams()
    def __init__(self, user_repository: UserRepository, auth_service: AuthService):
        self.user_repository = user_repository
        self.auth_service = auth_service

    def execute(self, email: str, password: str):
        user = self.authenticate_user(email, password)
        if not user:
            raise Exception("Incorrect email or password")
        access_token = self.create_access_token(data={"sub": user.email})
        return {"access_token": access_token, "token_type": "bearer"}

    def verify_password(self, plain_password: str, hashed_password: str):
        return self.auth_service.verify(plain_password, hashed_password)

    def get_password_hash(self, password: str):
        return self.auth_service.encrypt(password)

    def authenticate_user(self, email: str, password: str):
        user: User | None = self.user_repository.get_user(email)
        if not user:
            return False
        if not self.verify_password(password, user.password):
            return False
        return user

    def create_access_token(self, data: dict):
        return self.auth_service.create_access_token(data)

    def get_current_user(self, token: str):
        user_email = self.auth_service.get_current_user_email(token)
        user = self.user_repository.get_user(user_email)
        if not user:
            raise Exception("User not found")
        return user
