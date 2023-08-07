from fastapi import APIRouter, Query, Response
from typing import List, Tuple
from src.Game.QuizGame.Application.GetLeaderboardAndScoreUseCase import (
    GetLeaderboardAndScoreUseCase,
)
from src.Game.QuizGame.Application.SaveQuizGameUseCase import SaveQuizGameUseCase
from src.Game.QuizGame.Domain.QuizGame import QuizGame
from src.Game.QuizGame.Application.GetQuizGameUseCase import GetQuizGameUseCase
from src.Game.QuizGame.Domain.UserScore import UserScore
from src.Shared.Singleton import singleton


router = APIRouter()


@singleton
class FastAPIQuizGameController:
    def __init__(self):
        self.get_game_use_case = GetQuizGameUseCase()
        self.save_game_use_case = SaveQuizGameUseCase()
        self.get_leaderboard_and_score_use_case = GetLeaderboardAndScoreUseCase()

    def get_game(self, user_id: str) -> QuizGame:
        return self.get_game_use_case.execute(user_id=user_id)

    def save_game(self, game: QuizGame) -> bool:
        return self.save_game_use_case.execute(new_quiz_game=game)

    def get_leaderboard_and_score(self, user_id: str) -> Tuple[List[UserScore], int]:
        return self.get_leaderboard_and_score_use_case.execute(user_id=user_id)


def get_game_controller() -> FastAPIQuizGameController:
    return FastAPIQuizGameController()


@router.get("/quiz_game", status_code=200)
def get_game_endpoint(
    user_id: str = Query(None),
) -> QuizGame:
    return get_game_controller().get_game(user_id=user_id)


@router.put("/quiz_game")
def save_game_endpoint(game: QuizGame, response: Response):
    was_created = get_game_controller().save_game(game=game)
    if was_created:
        response.status_code = 201
    else:
        response.status_code = 200

    return {}


@router.get("/leaderboard", status_code=200)
def get_leaderboard_endpoint(
    user_id: str = Query(None),
) -> Tuple[List[UserScore], int]:
    return get_game_controller().get_leaderboard_and_score(user_id=user_id)
