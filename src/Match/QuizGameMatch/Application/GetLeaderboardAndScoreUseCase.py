import inject
from typing import List, Tuple
from src.Match.QuizGameMatch.Domain.QuizGameMatchRepository import (
    QuizGameMatchRepository,
)
from src.Match.QuizGameMatch.Domain.User.UserScore import UserScore
from src.Photo.Domain.PhotoFactory import PhotoFactory
from src.User.Domain.UserRepository import UserRepository


class GetLeaderboardAndScoreUseCase:
    @inject.autoparams()
    def __init__(
        self,
        quiz_game_repository: QuizGameMatchRepository,
        user_repository: UserRepository,
    ):
        self.quiz_game_repository = quiz_game_repository
        self.user_repository = user_repository

    def execute(self, user_id: str) -> Tuple[List[UserScore], int]:
        users_match, position = self.quiz_game_repository.get_leaderboard_and_score(
            user_id=user_id
        )

        users_scores = []

        for player in users_match:
            user = self.user_repository.get_by_id(player.user_id)
            user_score = UserScore(
                user_first_name=user.first_name,
                user_last_name=user.last_name,
                user_photo=PhotoFactory.create(img_path=user.photo.img_path),
                match_game_score=player.match_game_score,
                match_game_time=player.match_game_time,
            )
            users_scores.append(user_score)

        return users_scores, position
