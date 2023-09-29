from typing import List

from fastapi import APIRouter, HTTPException

from src.Game.Application.GetAllGamesUseCase import GetAllGamesUseCase
from src.Game.Domain.Game import Game
from src.Shared.Singleton import singleton

router = APIRouter()


@singleton
class FastAPIGameController:
    def __init__(self):
        self.get_game_use_case = GetAllGamesUseCase()

    def get_games(self) -> List[Game]:
        return self.get_game_use_case.execute()


def get_game_controller() -> FastAPIGameController:
    return FastAPIGameController()


@router.get("/get_games", status_code=200)
def get_all_games_endpoint() -> List[Game]:
    try:
        return get_game_controller().get_games()
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
