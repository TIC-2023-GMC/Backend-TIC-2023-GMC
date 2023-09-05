from pydantic import BaseModel
from fastapi import APIRouter, HTTPException
from src.Interaction.Like.Application.AddLikeUseCase import AddLikeUseCase
from src.Interaction.Like.Application.RemoveLikeUseCase import RemoveLikeUseCase
from src.Shared.Singleton import singleton

router = APIRouter()


@singleton
class FastAPILikeController:
    def __init__(self):
        self.add_like_use_case = AddLikeUseCase()
        self.remove_like_use_case = RemoveLikeUseCase()

    def add_like(self, pub_id: str, user_id: str, is_adoption: bool) -> None:
        self.add_like_use_case.execute(
            pub_id=pub_id, user_id=user_id, is_adoption=is_adoption
        )

    def remove_like(self, pub_id: str, user_id: str, is_adoption: bool) -> None:
        self.remove_like_use_case.execute(
            pub_id=pub_id, user_id=user_id, is_adoption=is_adoption
        )


def like_controller() -> FastAPILikeController:
    return FastAPILikeController()


@router.post("/add_like", status_code=200)
def add_like_endpoint(user_id: str, pub_id: str, is_adoption: bool) -> None:
    try:
        like_controller().add_like(
            pub_id=pub_id, user_id=user_id, is_adoption=is_adoption
        )
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.delete("/remove_like", status_code=200)
def remove_like_endpoint(user_id: str, pub_id: str, is_adoption: bool) -> None:
    try:
        like_controller().remove_like(
            pub_id=pub_id, user_id=user_id, is_adoption=is_adoption
        )
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
