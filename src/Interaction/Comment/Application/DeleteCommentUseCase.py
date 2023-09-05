import inject
from src.Interaction.Comment.Domain.CommentRepository import CommentRepository


class DeleteCommentUseCase:
    @inject.autoparams()
    def __init__(self, comment_repository: CommentRepository):
        self.comment_repository = comment_repository

    def execute(self, pub_id: str, comment_id: str, is_adoption: bool) -> None:
        return self.comment_repository.delete_comment(
            pub_id=pub_id, comment_id=comment_id, is_adoption=is_adoption
        )
