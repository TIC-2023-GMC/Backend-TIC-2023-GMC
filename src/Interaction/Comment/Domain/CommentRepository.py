import datetime
from abc import ABC, abstractmethod
from typing import List, Tuple

from src.Interaction.Comment.Domain.Comment import Comment
from src.User.Domain.User import User


class CommentRepository(ABC):
    @abstractmethod
    def add_comment(
        self, pub_id: str, user: User, comment_text: str, comment_date: datetime
    ) -> None:
        pass

    @abstractmethod
    def get_comments_by_id(
        self, pub_id: str, page_number: int, page_size: int
    ) -> Tuple[List[Comment], int]:
        pass

    @abstractmethod
    def update_comment(self, comment_id: str, comment_text: str) -> None:
        pass

    @abstractmethod
    def delete_comment(self, pub_id: str, comment_id: str) -> None:
        pass
