from typing import List, Tuple

import inject

from src.Match.QuizGameMatch.Domain.QuizGameMatchRepository import (
    QuizGameMatchRepository,
)
from src.Match.QuizGameMatch.Domain.User.UserScore import UserScore


class GetLeaderboardAndScoreUseCase:
    @inject.autoparams()
    def __init__(self, repository: QuizGameMatchRepository):
        self.repository = repository

    def execute(self, user_id: str) -> Tuple[List[UserScore], int]:
        return self.repository.get_leaderboard_and_score(user_id=user_id)
