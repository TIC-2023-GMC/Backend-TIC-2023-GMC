import inject

from src.Interaction.Comment.Domain.CommentRepository import CommentRepository
from src.Publication.Application.VerifyPublicationExistenceUseCase import (
    VerifyPublicationExistenceUseCase,
)


class DeleteCommentUseCase:
    @inject.autoparams()
    def __init__(self, comment_repository: CommentRepository):
        self.comment_repository = comment_repository
        self.verify_pub_existence_use_case = VerifyPublicationExistenceUseCase()

    def execute(self, pub_id: str, comment_id: str) -> None:
        if self.verify_pub_existence_use_case.execute(pub_id):
            return self.comment_repository.delete_comment(
                pub_id=pub_id, comment_id=comment_id
            )
        else:
            raise Exception("Publication not found")
