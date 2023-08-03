from fastapi import APIRouter, Query, Response
from src.Game.QuizGame.Application.SaveQuizGameUseCase import SaveQuizGameUseCase
from src.Game.QuizGame.Domain.QuizGame import QuizGame
from src.Game.QuizGame.Application.GetGameUseCase import GetQuizGameUseCase
from src.Shared.Singleton import singleton


router = APIRouter()


@singleton
class QuizGameFastAPIController:
    def __init__(self):
        self.get_game_use_case = GetQuizGameUseCase()
        self.save_game_use_case = SaveQuizGameUseCase()

    def get_game(self, user_id: str) -> QuizGame:
        return self.get_game_use_case.execute(user_id=user_id)

    def save_game(self, game: QuizGame) -> bool:
        return self.save_game_use_case.execute(new_quiz_game=game)


def get_game_controller() -> QuizGameFastAPIController:
    return QuizGameFastAPIController()


@router.get("/quiz_game", status_code=200)
def get_game_endpoint(
    user_id: str = Query(None),
) -> QuizGame:
    return get_game_controller().get_game(user_id=user_id)


@router.put("/quiz_game")
def save_game_endpoint(game: QuizGame, response: Response):
    was_created = get_game_controller().save_game(game=game)
    print(was_created)
    if was_created:
        response.status_code = 201
    else:
        response.status_code = 200

    return {}
