from typing import List
from src.Game.QuizGame.Domain.Question import Question
from src.Game.Domain.Game import Game


class QuizGame(Game):
    game_questions: List[Question]
    game_time: int
