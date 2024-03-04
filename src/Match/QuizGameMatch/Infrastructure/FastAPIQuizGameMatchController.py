from typing import Annotated, List, Tuple

from fastapi import APIRouter, Depends, HTTPException, Response

from src.Match.QuizGameMatch.Application.GetLeaderboardAndScoreUseCase import (
    GetLeaderboardAndScoreUseCase,
)
from src.Match.QuizGameMatch.Application.GetQuizGameMatchUseCase import (
    GetQuizGameMatchUseCase,
)
from src.Match.QuizGameMatch.Application.SaveQuizGameMatchUseCase import (
    SaveQuizGameMatchUseCase,
)
from src.Match.QuizGameMatch.Domain.QuizGameMatch import QuizGameMatch
from src.Match.QuizGameMatch.Domain.User.UserScore import UserScore
from src.Shared.Singleton import singleton
from src.User.Domain.User import User
from src.User.Infrastructure.FastAPIUserController import get_current_active_user

router = APIRouter()


@singleton
class FastAPIQuizGameController:
    def __init__(self):
        self.get_match_use_case = GetQuizGameMatchUseCase()
        self.save_match_use_case = SaveQuizGameMatchUseCase()
        self.get_leaderboard_and_score_use_case = GetLeaderboardAndScoreUseCase()

    def get_match(self, user_id: str) -> QuizGameMatch:
        return self.get_match_use_case.execute(user_id=user_id)

    def save_match(self, match: QuizGameMatch) -> bool:
        return self.save_match_use_case.execute(new_quiz_match=match)

    def get_leaderboard_and_score(self, user_id: str) -> Tuple[List[UserScore], int]:
        return self.get_leaderboard_and_score_use_case.execute(user_id=user_id)


def get_match_controller() -> FastAPIQuizGameController:
    return FastAPIQuizGameController()


@router.get("/quiz_game", status_code=200)
def get_match_endpoint(
    user: Annotated[User, Depends(get_current_active_user)],
) -> QuizGameMatch:
    try:
        return get_match_controller().get_match(user_id=user.id)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.put("/quiz_game")
def save_game_endpoint(match: QuizGameMatch, response: Response):
    was_created = get_match_controller().save_match(match=match)
    if was_created:
        response.status_code = 201
    else:
        response.status_code = 200

    return {}


@router.get("/leaderboard", status_code=200)
def get_leaderboard_endpoint(
    user: Annotated[User, Depends(get_current_active_user)],
) -> Tuple[List[UserScore], int]:
    try:
        return get_match_controller().get_leaderboard_and_score(user_id=user.id)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
