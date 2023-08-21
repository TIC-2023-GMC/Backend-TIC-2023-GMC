from abc import abstractmethod, ABC
from typing import List
from src.Game.Domain.Game import Game


class GameRepository(ABC):
    @abstractmethod
    def get_games(self) -> List[Game]:
        pass
