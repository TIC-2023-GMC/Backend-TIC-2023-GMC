from abc import abstractmethod, ABC
from src.Game.Domain.Game import Game
from src.Match.Domain.Match import Match


class MatchFactory(ABC):
    @abstractmethod
    def create_game(
        _id: str,
        user_id: str,
        match_name: str,
        match_game_score: int,
        match_game_time: int,
        match_game_onboarding: str,
    ) -> Match:
        pass
