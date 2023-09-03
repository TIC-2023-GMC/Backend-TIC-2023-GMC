from datetime import datetime
from typing import List
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

    def execute(
        self,
        pub_id: str,
        user_id: str,
        comment_text: str,
        comment_date: datetime,
        is_adoption: bool,
    ) -> None:
        return self.comment_repository.add_comment(
            pub_id=pub_id,
            user_id=user_id,
            comment_text=comment_text,
            comment_date=comment_date,
            is_adoption=is_adoption,
        )
