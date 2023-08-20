from abc import abstractmethod, ABC
from typing import List
from src.Game.Domain.GameInfo import GameInfo


class GameRepository(ABC):
    @abstractmethod
    def get_all_games(self) -> List[GameInfo]:
        pass
