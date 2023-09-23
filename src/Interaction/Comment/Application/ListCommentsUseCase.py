from typing import List, Tuple
import inject
from src.Interaction.Comment.Domain.Comment import Comment
from src.Interaction.Comment.Domain.CommentRepository import CommentRepository
from src.Publication.Application.VerifyPublicationExistenceUseCase import (
    VerifyPublicationExistenceUseCase,
)


class ListCommentsUseCase:
    @inject.autoparams()
    def __init__(self, comment_repository: CommentRepository):
        self.comment_repository = comment_repository
        self.verify_pub_existence_use_case = VerifyPublicationExistenceUseCase()

    def execute(
        self, pub_id: str, page_number: int, page_size: int
    ) -> Tuple[List[Comment], int]:
        if self.verify_pub_existence_use_case.execute(pub_id):
            return self.comment_repository.get_comments_by_id(
                pub_id=pub_id,
                page_number=page_number,
                page_size=page_size,
            )
        else:
            raise Exception("Publication not found")
