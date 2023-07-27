from abc import ABC, abstractmethod
from typing import List

from src.Publication.AdoptionPublication.Domain.AdoptionPublication import (
    AdoptionPublication,
)


class UserRepository(ABC):
    @abstractmethod
    def add_user(self, user):
        pass

    @abstractmethod
    def get_user(self, email, password):
        pass

    @abstractmethod
    def update_user(self, updated_user):
        pass

    @abstractmethod
    def get_by_id(self, id):
        pass

    @abstractmethod
    def add_favorite_pub(self, pub_id):
        pass

    @abstractmethod
    def remove_favorite_pub(self, pub_id):
        pass

    @abstractmethod
    def list_favorite_publications(
        self, favorite_adoption_publications: List[str]
    ) -> List[AdoptionPublication]:
        pass
