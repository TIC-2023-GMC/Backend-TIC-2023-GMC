from datetime import datetime
from typing import Annotated, List, Tuple

from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel

from src.Interaction.Comment.Application.CreateCommentUseCase import (
    CreateCommentUseCase,
)
from src.Interaction.Comment.Application.DeleteCommentUseCase import (
    DeleteCommentUseCase,
)
from src.Interaction.Comment.Application.ListCommentsUseCase import ListCommentsUseCase
from src.Interaction.Comment.Application.UpdateCommentUseCase import (
    UpdateCommentUseCase,
)
from src.Interaction.Comment.Domain.Comment import Comment
from src.Shared.Singleton import singleton
from src.User.Domain.User import User
from src.User.Infrastructure.FastAPIUserController import get_current_active_user

router = APIRouter()


class CommentData(BaseModel):
    pub_id: str
    comment_text: str
    comment_date: datetime


@singleton
class FastAPICommentController:
    def __init__(self):
        self.comment_list = ListCommentsUseCase()
        self.add_comment_use_case = CreateCommentUseCase()
        self.update_comment_use_case = UpdateCommentUseCase()
        self.delete_comment_use_case = DeleteCommentUseCase()

    def add_comment(
        self,
        pub_id: str,
        user: User,
        comment_text: str,
        comment_date: datetime,
    ) -> None:
        self.add_comment_use_case.execute(
            pub_id=pub_id,
            user=user,
            comment_text=comment_text,
            comment_date=comment_date,
        )

    def update_comment(self, comment_id: str, comment_text: str) -> None:
        self.update_comment_use_case.execute(comment_id, comment_text)

    def delete_comment(self, pub_id: str, comment_id: str) -> None:
        self.delete_comment_use_case.execute(pub_id=pub_id, comment_id=comment_id)

    def list_comments(
        self, pub_id: str, page_number: int, page_size: int
    ) -> Tuple[List[Comment], int]:
        return self.comment_list.execute(
            pub_id=pub_id,
            page_number=page_number,
            page_size=page_size,
        )


def get_comment_controller() -> FastAPICommentController:
    return FastAPICommentController()


@router.post("/add_comment", status_code=200)
def add_comment_endpoint(
    data: CommentData, user: Annotated[User, Depends(get_current_active_user)]
):
    try:
        get_comment_controller().add_comment(
            pub_id=data.pub_id,
            user=user,
            comment_text=data.comment_text,
            comment_date=data.comment_date,
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
def delete_comment_endpoint(pub_id: str, comment_id: str):
    try:
        get_comment_controller().delete_comment(pub_id=pub_id, comment_id=comment_id)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/list_comments", status_code=200)
def list_comments_endpoint(pub_id: str, page_number: int, page_size: int):
    try:
        return get_comment_controller().list_comments(
            pub_id=pub_id,
            page_number=page_number,
            page_size=page_size,
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
