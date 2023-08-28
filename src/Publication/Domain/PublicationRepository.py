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

    @abstractmethod
    def add_like(self, like: Like) -> None:
        pass

    @abstractmethod
    def remove_like_by_id(self, like_id: str) -> None:
        pass


    @abstractmethod
    def get_likes_by_pub_id(self, id: str) -> List[Like]:
        pass

    @abstractmethod
    def get_comments_by_pub_id(self, id: str) -> List[Comment]:
        pass

    @abstractmethod
    def add_comment(self, comment: Comment) -> None:
        pass
