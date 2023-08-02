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
            game_dict["_id"] = ObjectId()
            game_dict["user_id"] = ObjectId(game_dict["user_id"])
            self.game_quiz.insert_one(game_dict)
            was_created = True
        else:
            game_dict.pop("_id", None)
            self.game_quiz.update_one(
                {"_id": ObjectId(existing_game["_id"])}, {"$set": game_dict}
            )
        return was_created

    def get_game(self, user_id: str) -> QuizGame:
        game = self.game_quiz.find_one({"user_id": ObjectId(user_id)})
        if game:
            game["_id"] = str(game["_id"])
            game["user_id"] = str(game["user_id"])
            game = QuizGameFactory.create_game(**game)
        else:
            subset_size = 3

            """ questions = self.questions_quiz.find()
            game_questions = []
            if questions:
                for question in questions:
                    question.pop("_id", None)
                    game_questions.append(Question(**question))
                random.shuffle(game_questions) """

            questions = self.questions_quiz.aggregate(
                [{"$sample": {"size": subset_size}}]
            )
            game_questions = []
            if questions:
                for question in questions:
                    question.pop("_id", None)
                    game_questions.append(Question(**question))

            game = QuizGameFactory.create_game(
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
            self.save_game(game)
        return game
