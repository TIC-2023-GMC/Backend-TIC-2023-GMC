import inject
from typing import List, Tuple
from src.Game.QuizGame.Domain.QuizGameRepository import QuizGameRepository
from src.Game.QuizGame.Domain.UserScore import UserScore


class GetLeaderboardAndScoreUseCase:
    @inject.autoparams()
    def __init__(self, repository: QuizGameRepository):
        self.repository = repository

    def execute(self, user_id: str) -> Tuple[List[UserScore], int]:
        return self.repository.get_leaderboard_and_score(user_id=user_id)
