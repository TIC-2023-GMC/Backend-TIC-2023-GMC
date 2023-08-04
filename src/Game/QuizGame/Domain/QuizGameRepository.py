from abc import abstractmethod, ABC
from src.Game.QuizGame.Domain.QuizGame import QuizGame
from typing import List, Tuple
from src.Game.QuizGame.Domain.UserScore import UserScore


class QuizGameRepository(ABC):
    @abstractmethod
    def get_game(self) -> QuizGame:
        pass

    @abstractmethod
    def save_game(self, game: QuizGame) -> bool:
        pass

    @abstractmethod
    def get_leaderboard_and_score(self, user_id: str) -> Tuple[List[UserScore], int]:
        pass
