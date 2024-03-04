import inject

from src.Interaction.Comment.Domain.CommentRepository import CommentRepository


class UpdateCommentUseCase:
    @inject.autoparams()
    def __init__(self, comment_repository: CommentRepository):
        self.comment_repository = comment_repository

    def execute(self, comment_id: str, comment_text: str) -> None:
        return self.comment_repository.update_comment(comment_id, comment_text)
