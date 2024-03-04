from typing import List, Tuple

from bson import ObjectId

from src.Match.Domain.Match import Match
from src.Match.QuizGameMatch.Domain.Question.Question import Question
from src.Match.QuizGameMatch.Domain.QuizGameMatch import QuizGameMatch
from src.Match.QuizGameMatch.Domain.QuizGameMatchFactory import QuizGameMatchFactory
from src.Match.QuizGameMatch.Domain.QuizGameMatchRepository import (
    QuizGameMatchRepository,
)
from src.Shared.MongoClient import MongoDBConnection


class MongoDBQuizGameMatchRepository(QuizGameMatchRepository):
    db = MongoDBConnection().get_db()
    questions_quiz = db["questions_quiz"]
    game_quiz = db["game_quiz"]

    def save_match(self, match: QuizGameMatch) -> bool:
        was_created = False
        game_dict = match.dict()
        game_dict["_id"] = ObjectId()
        game_dict["user_id"] = ObjectId(game_dict["user_id"])
        existing_game = self.game_quiz.find_one({"user_id": game_dict["user_id"]})
        if existing_game is None:
            self.game_quiz.insert_one(game_dict)
            was_created = True
        else:
            game_dict.pop("_id", None)
            self.game_quiz.update_one(
                {"_id": ObjectId(existing_game["_id"])}, {"$set": game_dict}
            )
        return was_created

    def get_match(self, user_id: str) -> QuizGameMatch:
        existing_game = self.game_quiz.find_one({"user_id": ObjectId(user_id)})
        subset_size = 10
        match_game_questions = []
        questions = self.questions_quiz.aggregate([{"$sample": {"size": subset_size}}])
        for question in questions:
            question.pop("_id", None)
            match_game_questions.append(Question(**question))

        if existing_game:
            existing_game["_id"] = str(existing_game["_id"])
            existing_game["user_id"] = str(existing_game["user_id"])
            existing_game["match_game_questions"] = match_game_questions
            existing_game = QuizGameMatchFactory.create_game(**existing_game)
        else:
            existing_game = QuizGameMatchFactory.create_game(
                _id=None,
                user_id=user_id,
                match_name="Quiz Game Match",
                match_game_score=0,
                match_game_time=0,
                match_game_onboarding="N/A",
                match_game_questions=match_game_questions,
            )
        self.save_match(existing_game)
        return existing_game

    def get_leaderboard_and_score(self, user_id: str) -> Tuple[List[Match], int]:
        player_game = self.game_quiz.find_one({"user_id": ObjectId(user_id)})
        leaderboard_position = self.game_quiz.count_documents(
            {"match_game_score": {"$gt": player_game["match_game_score"]}}
        )

        leaderboard = self.game_quiz.find().sort("match_game_score", -1).limit(4)

        leaderboard_list = []

        for player in leaderboard:
            player["_id"] = str(player["_id"])
            player["user_id"] = str(player["user_id"])
            score_info = Match(
                _id=player["_id"],
                user_id=player["user_id"],
                match_name=player["match_name"],
                match_game_score=player["match_game_score"],
                match_game_time=player["match_game_time"],
                match_game_onboarding=player["match_game_onboarding"],
            )
            leaderboard_list.append(score_info)

        return leaderboard_list, leaderboard_position + 1
