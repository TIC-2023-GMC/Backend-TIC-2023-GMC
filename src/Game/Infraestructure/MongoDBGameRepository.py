from src.Game.Domain.GameInfo import GameInfo
from typing import List
from src.Game.Domain.GameRepository import GameRepository
from src.Shared.MongoClient import MongoDBConnection


class MongoDBGameRepository(GameRepository):
    db = MongoDBConnection().get_db()
    games_collection = db["games"]

    def get_all_games(self) -> List[GameInfo]:
        document = self.games_collection.find()
        games_list = []
        for game in document:
            game.pop("_id", None)
            games_list.append(GameInfo(**game))
        return games_list
