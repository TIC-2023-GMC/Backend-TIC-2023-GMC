from abc import ABC, abstractmethod
from datetime import timedelta


class AuthService(ABC):
    access_token_expire_minutes: timedelta

    @abstractmethod
    def encrypt(self, password: str) -> str:
        pass

    @abstractmethod
    def verify(self, password: str, hashed_password: str) -> bool:
        pass

    @abstractmethod
    def create_access_token(self, data: dict) -> str:
        pass

    @abstractmethod
    def get_current_user_email(self, token: str) -> dict:
        pass
