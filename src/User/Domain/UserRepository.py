from abc import ABC, abstractmethod
from typing import List, Tuple
from src.User.Domain.User import User

from src.Publication.AdoptionPublication.Domain.AdoptionPublication import (
    AdoptionPublication,
)


class UserRepository(ABC):
    @abstractmethod
    def add_user(self, user) -> None:
        pass

    @abstractmethod
    def get_user(self, email, password) -> User:
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
        favorite_adoption_publications: List[str],
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
