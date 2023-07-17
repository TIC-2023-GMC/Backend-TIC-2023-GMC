from abc import ABC, abstractmethod
from datetime import date
from typing import List, Tuple
from Interaction.Comment.Domain.Comment import Comment
from Interaction.Like.Domain.Like import Like

from Publication.Domain.Publication import Publication


class PublicationRepository(ABC):
    @abstractmethod
    def add_publication(self, publication: Publication):
        pass

    @abstractmethod
    def get_all(self, pageNumber: int, pageSize: int) -> Tuple[List[Publication], int]:
        pass

    @abstractmethod
    def get_by_id(self, id: int) -> Publication:
        pass

    @abstractmethod
    def get_by_filters(
        self, species: str, date: date, location: str, pageNumber: int, pageSize: int
    ) -> Tuple[List[Publication], int]:
        pass

    @abstractmethod
    def add_like(self, like: Like):
        pass

    @abstractmethod
    def remove_like_by_id(self, like_id: int):
        pass

    @abstractmethod
    def get_likes_by_pub_id(self, id: int) -> List[Like]:
        pass

    @abstractmethod
    def get_comments_by_pub_id(self, id: int) -> List[Comment]:
        pass

    @abstractmethod
    def add_comment(self, comment: Comment):
        pass
