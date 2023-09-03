import inject
from src.Interaction.Comment.Domain.CommentRepository import CommentRepository
from src.Interaction.Comment.Infrastructure.MongoDBCommentRepository import (
    MongoDBCommentRepository,
)
from src.Interaction.Comment.Domain.Comment import Comment


class CreateCommentUseCase:
    @inject.params(comment_repository=MongoDBCommentRepository)
    def __init__(self, comment_repository: CommentRepository):
        self.comment_repository = comment_repository

    def execute(self, comment: Comment, pub_id: str, is_adoption: bool) -> None:
        return self.comment_repository.add_comment(
            comment=comment, pub_id=pub_id, is_adoption=is_adoption
        )
