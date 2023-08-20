from typing import List
import inject
from src.Game.Domain.GameInfo import GameInfo
from src.Game.Domain.GameRepository import GameRepository


class GetAllGamesUseCase:
    @inject.autoparams()
    def __init__(self, repository: GameRepository):
        self.repository = repository

    def execute(self) -> List[GameInfo]:
        return self.repository.get_all_games()
