from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException, Response
from src.Match.WordleGameMatch.Application.GetWordleMatchUseCase import (
    GetWordleMatchUseCase,
)
from src.Match.WordleGameMatch.Application.SaveWordleMatchUseCase import (
    SaveWordleMatchUseCase,
)
from src.Match.WordleGameMatch.Domain.WordleMatch import WordleMatch

from src.Shared.Singleton import singleton
from src.User.Domain.User import User
from src.User.Infrastructure.FastAPIUserController import get_current_active_user


router = APIRouter()


@singleton
class FastAPIWordleMatchController:
    def __init__(self):
        self.get_wordle_match_use_case = GetWordleMatchUseCase()
        self.save_wordle_match_use_case = SaveWordleMatchUseCase()

    def get_worldle_match(self, user_id: str):
        return self.get_wordle_match_use_case.execute(user_id=user_id)

    def save_wordle_match(self, match: WordleMatch) -> bool:
        return self.save_wordle_match_use_case.execute(match=match)


def get_wordle_match_controller() -> FastAPIWordleMatchController:
    return FastAPIWordleMatchController()


@router.get("/get_wordle_match", status_code=200)
def get_wordle_match(
    user: Annotated[User, Depends(get_current_active_user)],
) -> WordleMatch:
    try:
        return get_wordle_match_controller().get_worldle_match(user_id=user.id)
    except Exception as e:
        print(e)
        raise HTTPException(status_code=400, detail=str(e))


@router.put("/put_wordle_match")
def save_wordle_match(match: WordleMatch, response: Response):
    was_created = get_wordle_match_controller().save_wordle_match(match=match)
    if was_created:
        response.status_code = 201
    else:
        response.status_code = 200
    return {}
