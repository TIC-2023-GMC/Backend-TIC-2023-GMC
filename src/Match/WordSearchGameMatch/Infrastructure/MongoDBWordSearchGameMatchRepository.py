from typing import List, Tuple

from bson import ObjectId
from src.Match.Domain.Match import Match
from src.Match.QuizGameMatch.Domain.Question.Question import Question
from src.Match.QuizGameMatch.Domain.QuizGameMatch import QuizGameMatch
from src.Match.QuizGameMatch.Domain.QuizGameMatchFactory import QuizGameMatchFactory
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

        self.game_quiz.insert_one(game_dict)
        was_created = True

        return was_created

    def get_match(self, user_id: str) -> WordSearchGameMatch:
        existing_game = self.game_word_search.find_one({"user_id": ObjectId(user_id)})
        topic = self.topics_word_search.aggregate([{"$sample": {"size": 1}}])
        topic.pop("_id", None)

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
