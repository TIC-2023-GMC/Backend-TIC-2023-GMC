import datetime
from abc import ABC, abstractmethod
from typing import List, Tuple

from src.Publication.Domain.Publication import Publication


class PublicationRepository(ABC):
    @abstractmethod
    def add_publication(self, publication: Publication):
        pass

    @abstractmethod
    def get_all(
        self,
        species: str,
        date: datetime,
        page_number: int,
        page_size: int,
        user_id: str,
        location: str = None,
    ) -> Tuple[List[Publication], int]:
        pass

    @abstractmethod
    def get_by_id(self, id: str) -> Publication:
        pass

    @abstractmethod
    def add_like(self, pub_id: str, user_id: str) -> None:
        pass

    @abstractmethod
    def remove_like(self, pub_id: str, user_id: str) -> None:
        pass
