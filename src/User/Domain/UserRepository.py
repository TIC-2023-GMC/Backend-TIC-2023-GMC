from abc import ABC, abstractmethod
from typing import List, Tuple

from src.Publication.AdoptionPublication.Domain.AdoptionPublication import (
    AdoptionPublication,
)
from src.User.Domain.User import User


class UserRepository(ABC):
    @abstractmethod
    def add_user(self, user: User) -> None:
        pass

    @abstractmethod
    def get_user(self, email: str, mobile_phone: str = None) -> User:
        pass

    @abstractmethod
    def update_user(self, updated_user) -> None:
        pass

    @abstractmethod
    def get_by_id(self, _id: str) -> User:
        pass

    @abstractmethod
    def add_favorite_pub(self, pub_id: str, user_id: str) -> None:
        pass

    @abstractmethod
    def remove_favorite_pub(self, pub_id: str, user_id: str) -> None:
        pass

    @abstractmethod
    def list_favorite_publications(
        self,
        user_id: str,
        page_number: int,
        page_size: int,
    ) -> Tuple[List[AdoptionPublication], int]:
        pass

    @abstractmethod
    def list_my_publications(
        self,
        page_number: int,
        page_size: int,
        user_id: str,
    ) -> Tuple[List[AdoptionPublication], int]:
        pass
