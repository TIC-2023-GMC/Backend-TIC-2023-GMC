from typing import List

from src.Game.Domain.Game import Game
from src.Game.Domain.GameRepository import GameRepository
from src.Shared.MongoClient import MongoDBConnection


class MongoDBGameRepository(GameRepository):
    db = MongoDBConnection().get_db()
    games_collection = db["games"]

    def get_games(self) -> List[Game]:
        document = self.games_collection.find()
        games_list = []
        for game in document:
            game.pop("_id", None)
            games_list.append(Game(**game))
        return games_list
