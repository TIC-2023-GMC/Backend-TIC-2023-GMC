from abc import abstractmethod, ABC
from typing import List, Tuple

from src.Match.QuizGameMatch.Domain.QuizGameMatch import QuizGameMatch
from src.Match.QuizGameMatch.Domain.User.UserScore import UserScore


class QuizGameMatchRepository(ABC):
    @abstractmethod
    def get_match(self) -> QuizGameMatch:
        pass

    @abstractmethod
    def save_match(self, match: QuizGameMatch) -> bool:
        pass

    @abstractmethod
    def get_leaderboard_and_score(self, user_id: str) -> Tuple[List[UserScore], int]:
        pass
