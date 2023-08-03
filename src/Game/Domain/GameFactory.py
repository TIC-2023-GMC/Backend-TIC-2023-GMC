from abc import abstractmethod, ABC
from src.Game.Domain.Game import Game


class GameFactory(ABC):
    @abstractmethod
    def create_game(
        _id: str,
        game_name: str,
        game_description: str,
        game_image: str,
        game_category: str,
        game_score: int,
    ) -> Game:
        pass
