import datetime

import inject

from src.Interaction.Comment.Domain.CommentRepository import CommentRepository
from src.Publication.Application.VerifyPublicationExistenceUseCase import (
    VerifyPublicationExistenceUseCase,
)
from src.User.Domain.User import User


class CreateCommentUseCase:
    @inject.autoparams()
    def __init__(self, comment_repository: CommentRepository):
        self.comment_repository = comment_repository
        self.verify_pub_existence_use_case = VerifyPublicationExistenceUseCase()

    def execute(
        self,
        pub_id: str,
        user: User,
        comment_text: str,
        comment_date: datetime,
    ) -> None:
        if self.verify_pub_existence_use_case.execute(pub_id):
            return self.comment_repository.add_comment(
                pub_id=pub_id,
                user=user,
                comment_text=comment_text,
                comment_date=comment_date,
            )
        else:
            raise Exception("Publication not found")
