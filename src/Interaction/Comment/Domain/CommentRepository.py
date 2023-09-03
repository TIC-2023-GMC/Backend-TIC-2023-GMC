from abc import ABC, abstractmethod
from typing import List, Tuple

from src.Interaction.Comment.Domain.Comment import Comment


class CommentRepository(ABC):
    @abstractmethod
    def add_comment(self, comment: Comment, pub_id: str, is_adoption: bool) -> None:
        pass

    @abstractmethod
    def get_comments_by_id(
        self, comments_id: List[str], page_number: int, page_size: int
    ) -> Tuple[List[Comment], int]:
        pass
