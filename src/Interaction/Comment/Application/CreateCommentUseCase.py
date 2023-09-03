import inject
from src.Interaction.Comment.Domain.CommentRepository import CommentRepository
from src.Interaction.Comment.Infrastructure.MongoDBCommentRepository import (
    MongoDBCommentRepository,
)


class CreateCommentUseCase:
    @inject.params(comment_repository=MongoDBCommentRepository)
    def __init__(self, comment_repository: CommentRepository):
        self.comment_repository = comment_repository

    def execute(
        self,
        pub_id: str,
        user_id: str,
        comment_text: str,
        is_adoption: bool,
    ) -> None:
        return self.comment_repository.add_comment(
            pub_id=pub_id,
            user_id=user_id,
            comment_text=comment_text,
            is_adoption=is_adoption,
        )
