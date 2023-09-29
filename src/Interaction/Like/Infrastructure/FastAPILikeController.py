from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel

from src.Interaction.Like.Application.AddAdoptionLikeUseCase import (
    AddAdoptionLikeUseCase,
)
from src.Interaction.Like.Application.AddExperienceLikeUseCase import (
    AddExperienceLikeUseCase,
)
from src.Interaction.Like.Application.RemoveAdoptionLikeUseCase import (
    RemoveAdoptionLikeUseCase,
)
from src.Interaction.Like.Application.RemoveExperienceLikeUseCase import (
    RemoveExperienceLikeUseCase,
)
from src.Shared.Singleton import singleton
from src.User.Domain.User import User
from src.User.Infrastructure.FastAPIUserController import get_current_user

router = APIRouter()


class LikeRequest(BaseModel):
    pub_id: str
    is_adoption: bool


@singleton
class FastAPILikeController:
    def __init__(self):
        self.add_experience_like_use_case = AddExperienceLikeUseCase()
        self.remove_experience_like_use_case = RemoveExperienceLikeUseCase()
        self.add_adoption_like_use_case = AddAdoptionLikeUseCase()
        self.remove_adoption_like_use_case = RemoveAdoptionLikeUseCase()

    def add_like(self, pub_id: str, user_id: str, is_adoption: bool) -> None:
        if is_adoption:
            return self.add_adoption_like_use_case.execute(
                pub_id=pub_id, user_id=user_id
            )
        else:
            return self.add_experience_like_use_case.execute(
                pub_id=pub_id, user_id=user_id
            )

    def remove_like(self, pub_id: str, user_id: str, is_adoption: bool) -> None:
        if is_adoption:
            return self.remove_adoption_like_use_case.execute(
                pub_id=pub_id, user_id=user_id
            )
        else:
            return self.remove_experience_like_use_case.execute(
                pub_id=pub_id, user_id=user_id
            )


def like_controller() -> FastAPILikeController:
    return FastAPILikeController()


@router.post("/add_like", status_code=200)
def add_like_endpoint(
    like: LikeRequest,
    user: User = Depends(get_current_user),
) -> None:
    try:
        like_controller().add_like(
            pub_id=like.pub_id, user_id=user.id, is_adoption=like.is_adoption
        )
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.delete("/remove_like", status_code=200)
def remove_like_endpoint(
    like: LikeRequest,
    user: User = Depends(get_current_user),
) -> None:
    try:
        like_controller().remove_like(
            pub_id=like.pub_id, user_id=user.id, is_adoption=like.is_adoption
        )
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
