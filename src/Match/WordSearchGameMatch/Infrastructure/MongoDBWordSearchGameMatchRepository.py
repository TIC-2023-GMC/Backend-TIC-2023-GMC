from bson import ObjectId

from src.Match.WordSearchGameMatch.Domain.Statement.Statement import Statement
from src.Match.WordSearchGameMatch.Domain.WordSearchGameMatch import WordSearchGameMatch
from src.Match.WordSearchGameMatch.Domain.WordSearchGameMatchFactory import (
    WordSearchGameMatchFactory,
)
from src.Match.WordSearchGameMatch.Domain.WordSearchGameMatchRepository import (
    WordSearchGameMatchRepository,
)
from src.Shared.MongoClient import MongoDBConnection


class MongoDBWordSearchGameMatchRepository(WordSearchGameMatchRepository):
    db = MongoDBConnection().get_db()
    topics_word_search = db["topics_word_search"]
    game_word_search = db["game_word_search"]

    def save_match(self, match: WordSearchGameMatch) -> bool:
        was_created = False
        game_dict = match.dict()
        game_dict["_id"] = ObjectId()
        game_dict["user_id"] = ObjectId(game_dict["user_id"])

        game_dict.pop("match_game_score", None)
        game_dict.pop("match_game_time", None)

        existing_game = self.game_word_search.find_one(
            {"user_id": game_dict["user_id"]}
        )

        if existing_game is None:
            self.game_word_search.insert_one(game_dict)
            was_created = True
        else:
            game_dict.pop("_id", None)
            self.game_word_search.update_one(
                {"_id": ObjectId(existing_game["_id"])}, {"$set": game_dict}
            )
        return was_created

    def get_match(self, user_id: str) -> WordSearchGameMatch:
        existing_game = self.game_word_search.find_one({"user_id": ObjectId(user_id)})
        topic_cursor = self.topics_word_search.aggregate([{"$sample": {"size": 1}}])

        topic = next(topic_cursor, None)
        topic.pop("_id")

        statements = topic.get("statements", [])
        statements_objs = []

        for index, statement in enumerate(statements):
            if index % 2 != 0:
                statement["orientation"] = "horizontal"
            else:
                statement["orientation"] = "vertical"
            statement["number"] = index + 1
            statement_obj = Statement(**statement)
            statements_objs.append(statement_obj)

        topic["statements"] = statements_objs

        if existing_game:
            existing_game["_id"] = str(existing_game["_id"])
            existing_game["user_id"] = str(existing_game["user_id"])
            existing_game["match_game_topic"] = topic
            existing_game = WordSearchGameMatchFactory.create_game(**existing_game)
        else:
            existing_game = WordSearchGameMatchFactory.create_game(
                _id=None,
                user_id=user_id,
                match_name="Word Search Game Match",
                match_game_onboarding="N/A",
                match_game_topic=topic,
            )
        self.save_match(existing_game)
        return existing_game
