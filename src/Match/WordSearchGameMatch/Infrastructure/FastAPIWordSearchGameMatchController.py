from fastapi import APIRouter, Depends, HTTPException
from typing import Annotated

from src.Match.WordSearchGameMatch.Application.GetQuizGameMatchUseCase import (
    GetWordSearchGameMatchUseCase,
)
from src.Match.WordSearchGameMatch.Domain.WordSearchGameMatch import WordSearchGameMatch
from src.Shared.Singleton import singleton
from src.User.Domain.User import User
from src.User.Infrastructure.FastAPIUserController import get_current_active_user

router = APIRouter()


@singleton
class FastAPIWordSearchGameController:
    def __init__(self):
        self.get_match_use_case = GetWordSearchGameMatchUseCase()

    def get_match(self, user_id: str) -> WordSearchGameMatch:
        return self.get_match_use_case.execute(user_id=user_id)


def get_match_controller() -> FastAPIWordSearchGameController:
    return FastAPIWordSearchGameController()


@router.get("/get_match", status_code=200)
def get_match_endpoint(
    user: Annotated[User, Depends(get_current_active_user)],
) -> WordSearchGameMatch:
    try:
        return get_match_controller().get_match(user_id=user.id)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
