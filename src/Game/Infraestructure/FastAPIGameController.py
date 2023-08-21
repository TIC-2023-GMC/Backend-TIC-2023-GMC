from fastapi import APIRouter
from typing import List, Tuple
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
    return get_game_controller().get_games()
