from typing import List, Tuple
from fastapi import APIRouter, HTTPException
from src.Interaction.Comment.Domain.Comment import Comment
from src.Interaction.Comment.Application.ListCommentsUseCase import ListCommentsUseCase
from src.Shared.Singleton import singleton


router = APIRouter()


@singleton
class FastAPICommentController:
    def __init__(self):
        self.commert_list = ListCommentsUseCase()

    def list_comments(
        self,
        comments_id: List[str],
        page_number: int,
        page_size: int,
    ) -> Tuple[List[Comment], int]:
        return self.commert_list.execute(
            comments_id=comments_id,
            page_number=page_number,
            page_size=page_size,
        )


def get_comment_controller() -> FastAPICommentController:
    return FastAPICommentController()


@router.post("/list_comments", status_code=200)
def list_comments_endpoint(
    comments_id: List[str],
    page_number: int,
    page_size: int,
):
    try:
        return get_comment_controller().list_comments(
            comments_id=comments_id,
            page_number=page_number,
            page_size=page_size,
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
