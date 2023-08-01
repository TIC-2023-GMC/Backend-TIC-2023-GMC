from typing import List
from src.Game.QuizGame.Domain.Question import Question
from src.Photo.Domain.Photo import Photo
from src.Game.Domain.GameFactory import GameFactory
from src.Game.Domain.Game import Game
from src.Game.QuizGame.Domain.QuizGame import QuizGame


class QuizGameFactory(GameFactory):
    @staticmethod
    def create_game(
        _id: str,
        game_name: str,
        game_description: str,
        game_image: Photo,
        game_category: str,
        game_score: int,
        game_questions: List[Question],
        game_time: int,
        user_id: str,
    ) -> Game:
        return QuizGame(
            _id=_id,
            game_name=game_name,
            game_description=game_description,
            game_image=game_image,
            game_category=game_category,
            game_score=game_score,
            game_questions=game_questions,
            game_time=game_time,
            user_id=user_id,
        )
