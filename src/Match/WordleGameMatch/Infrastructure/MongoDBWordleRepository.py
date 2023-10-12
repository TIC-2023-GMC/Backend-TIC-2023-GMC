from bson import ObjectId
from src.Match.WordleGameMatch.Domain.WordleMatch import WordleMatch
from src.Match.WordleGameMatch.Domain.WordleMatchFactory import WordleMatchFactory
from src.Match.WordleGameMatch.Domain.WordleMatchRepository import WordleMatchRepository
from src.Shared.MongoClient import MongoDBConnection


class MongoDBWordleMatchRepository(WordleMatchRepository):
    db = MongoDBConnection().get_db()
    wordle_match = db["wordle_match"]
    words_wordle = db["words_wordle"]

    def get_match(self, user_id: str) -> WordleMatch:
        existing_match = self.wordle_match.find_one({"user_id": ObjectId(user_id)})
        pipeline = [{"$sample": {"size": 1}}]
        wordle_words_data = list(self.words_wordle.aggregate(pipeline))[0]
        if existing_match:
            existing_match["_id"] = str(existing_match["_id"])
            existing_match["user_id"] = str(existing_match["user_id"])
            existing_match["wordle_game_clue"] = wordle_words_data["wordle_game_clue"]
            existing_match["wordle_game_description"] = wordle_words_data[
                "wordle_game_description"
            ]
            existing_match["wordle_game_words"] = wordle_words_data["wordle_game_words"]
            existing_match = WordleMatchFactory.create_game(**existing_match)
        else:
            existing_match = WordleMatchFactory.create_game(
                _id=None,
                user_id=user_id,
                match_name="Wordle Game Match",
                match_game_score=0,
                match_game_time=0,
                match_game_onboarding="N/A",
                wordle_game_clue=wordle_words_data["wordle_game_clue"],
                wordle_game_description=wordle_words_data["wordle_game_description"],
                wordle_game_words=wordle_words_data["wordle_game_words"],
            )
        self.save_match(existing_match)
        return existing_match

    def save_match(self, match: WordleMatch) -> bool:
        was_created = False
        match_dict = match.dict()
        match_dict["_id"] = ObjectId()
        match_dict["user_id"] = ObjectId(match_dict["user_id"])
        existing_match = self.wordle_match.find_one({"user_id": match_dict["user_id"]})
        if existing_match is None:
            self.wordle_match.insert_one(match_dict)
            was_created = True
        else:
            match_dict.pop("_id", None)
            self.wordle_match.update_one(
                {"_id": ObjectId(existing_match["_id"])}, {"$set": match_dict}
            )
        return was_created
