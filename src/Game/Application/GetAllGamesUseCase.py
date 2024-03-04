from typing import List

import inject

from src.Game.Domain.Game import Game
from src.Game.Domain.GameRepository import GameRepository


class GetAllGamesUseCase:
    @inject.autoparams()
    def __init__(self, repository: GameRepository):
        self.repository = repository

    def execute(self) -> List[Game]:
        return self.repository.get_games()
