import random
from bson import ObjectId
from src.Photo.Domain.PhotoFactory import PhotoFactory
from src.Game.QuizGame.Domain.QuizGame import QuizGame
from src.Game.QuizGame.Domain.QuizGameFactory import QuizGameFactory
from src.Game.QuizGame.Domain.QuizGame import QuizGame
from src.Game.QuizGame.Domain.Question import Question
from src.Game.QuizGame.Domain.QuizGameRepository import QuizGameRepository
from src.Shared.MongoClient import MongoDBConnection


class MongoDBQuizGameRepository(QuizGameRepository):
    db = MongoDBConnection().get_db()
    questions_quiz = db["questions_quiz"]
    game_quiz = db["game_quiz"]

    def save_game(self, game: QuizGame) -> bool:
        was_created = False
        game_dict = game.dict()
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

    def get_game(self, user_id: str) -> QuizGame:
        existing_game = self.game_quiz.find_one({"user_id": ObjectId(user_id)})
        subset_size = 2
        game_questions = []
        questions = self.questions_quiz.aggregate([{"$sample": {"size": subset_size}}])
        for question in questions:
            question.pop("_id", None)
            game_questions.append(Question(**question))

        if existing_game:
            existing_game["_id"] = str(existing_game["_id"])
            existing_game["user_id"] = str(existing_game["user_id"])
            existing_game["game_questions"] = game_questions
            existing_game = QuizGameFactory.create_game(**existing_game)
        else:
            existing_game = QuizGameFactory.create_game(
                _id=None,
                game_name="QuizGame",
                game_description="",
                game_image=PhotoFactory.create(_id="", img_path=""),
                game_category="",
                game_score=0,
                game_questions=game_questions,
                game_time=0,
                user_id=user_id,
            )
        self.save_game(existing_game)
        return existing_game
