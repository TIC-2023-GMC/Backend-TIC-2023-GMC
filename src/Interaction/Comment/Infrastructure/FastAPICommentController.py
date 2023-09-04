from pydantic import BaseModel
from typing import List, Tuple
from fastapi import APIRouter, HTTPException
from src.Interaction.Comment.Application.CreateCommentUseCase import (
    CreateCommentUseCase,
)
from src.Interaction.Comment.Application.DeleteCommentUseCase import (
    DeleteCommentUseCase,
)
from src.Interaction.Comment.Application.UpdateCommentUseCase import (
    UpdateCommentUseCase,
)
from src.Interaction.Comment.Domain.Comment import Comment
from src.Interaction.Comment.Application.ListCommentsUseCase import ListCommentsUseCase
from src.Shared.Singleton import singleton


router = APIRouter()


class CommentData(BaseModel):
    pub_id: str
    user_id: str
    comment_text: str
    is_adoption: bool


@singleton
class FastAPICommentController:
    def __init__(self):
        self.commert_list = ListCommentsUseCase()
        self.add_comment_use_case = CreateCommentUseCase()
        self.update_comment_use_case = UpdateCommentUseCase()
        self.delete_comment_use_case = DeleteCommentUseCase()

    def add_comment(
        self,
        pub_id: str,
        user_id: str,
        comment_text: str,
        is_adoption: bool,
    ) -> None:
        self.add_comment_use_case.execute(
            pub_id=pub_id,
            user_id=user_id,
            comment_text=comment_text,
            is_adoption=is_adoption,
        )

    def update_comment(self, comment_id: str, comment_text: str) -> None:
        self.update_comment_use_case.execute(comment_id, comment_text)

    def delete_comment(self, pub_id: str, comment_id: str, is_adoption: bool) -> None:
        self.delete_comment_use_case.execute(
            pub_id=pub_id, comment_id=comment_id, is_adoption=is_adoption
        )

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


@router.post("/add_comment", status_code=200)
def add_comment_endpoint(data: CommentData):
    try:
        get_comment_controller().add_comment(
            pub_id=data.pub_id,
            user_id=data.user_id,
            comment_text=data.comment_text,
            is_adoption=data.is_adoption,
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/update_comment", status_code=200)
def update_comment_endpoint(comment_id: str, comment_text: str):
    try:
        get_comment_controller().update_comment(
            comment_id=comment_id,
            comment_text=comment_text,
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/delete_comment", status_code=200)
def delete_comment_endpoint(pub_id: str, comment_id: str, is_adoption: bool):
    try:
        get_comment_controller().delete_comment(
            pub_id=pub_id,
            comment_id=comment_id,
            is_adoption=is_adoption,
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


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
