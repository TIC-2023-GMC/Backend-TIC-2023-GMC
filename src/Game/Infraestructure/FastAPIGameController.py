from fastapi import APIRouter
from typing import List, Tuple
from src.Game.Application.GetAllGamesUseCase import GetAllGamesUseCase
from src.Game.Domain.GameInfo import GameInfo
from src.Shared.Singleton import singleton

router = APIRouter()


@singleton
class FastAPIGameController:
    def __init__(self):
        self.get_all_game_use_case = GetAllGamesUseCase()

    def get_all_games(self) -> List[GameInfo]:
        return self.get_all_game_use_case.execute()


def get_all_game_controller() -> FastAPIGameController:
    return FastAPIGameController()


@router.get("/get_all_games", status_code=200)
def get_all_games_endpoint() -> List[GameInfo]:
    return get_all_game_controller().get_all_games()
