from typing import List, Tuple
import inject
from src.Interaction.Comment.Domain.Comment import Comment
from src.Interaction.Comment.Domain.CommentRepository import CommentRepository


class ListCommentsUseCase:
    @inject.autoparams()
    def __init__(self, comment_repository: CommentRepository):
        self.comment_repository = comment_repository

    def execute(
        self, pub_id: str, page_number: int, page_size: int, is_adoption: bool
    ) -> Tuple[List[Comment], int]:
        return self.comment_repository.get_comments_by_id(
            pub_id=pub_id, page_number=page_number, page_size=page_size, is_adoption=is_adoption
        )
