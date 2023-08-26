from typing import List, Tuple
import inject
from src.Interaction.Comment.Domain.Comment import Comment
from src.Interaction.Comment.Domain.CommentRepository import CommentRepository


class ListCommentsUseCase:
    @inject.autoparams()
    def __init__(self, comment_repository: CommentRepository):
        self.comment_repository = comment_repository

    def execute(
        self, comments_id: List[str], page_number: int, page_size: int
    ) -> Tuple[List[Comment], int]:
        return self.comment_repository.get_comments_by_id(
            comments_id=comments_id, page_number=page_number, page_size=page_size
        )
