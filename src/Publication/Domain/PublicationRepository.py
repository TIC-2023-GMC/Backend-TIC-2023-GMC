from abc import ABC, abstractmethod
from typing import List, Tuple
from src.Interaction.Comment.Domain.Comment import Comment
from src.Interaction.Like.Domain.Like import Like
from src.Publication.Domain.Publication import Publication


class PublicationRepository(ABC):
    @abstractmethod
    def add_publication(self, publication: Publication):
        pass

    @abstractmethod
    def get_all(
        self, species: str, date: str, location: str, page_number: int, page_size: int
    ) -> Tuple[List[Publication], int]:
        pass

    @abstractmethod
    def get_by_id(self, id: str) -> Publication:
        pass
