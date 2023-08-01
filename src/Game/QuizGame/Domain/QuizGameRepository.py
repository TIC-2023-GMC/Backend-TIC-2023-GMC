from abc import abstractmethod, ABC
from src.Game.QuizGame.Domain.QuizGame import QuizGame
from src.Game.QuizGame.Domain.Question import Question
from typing import List


class QuizGameRepository(ABC):
    @abstractmethod
    def get_game(self) -> QuizGame:
        pass

    @abstractmethod
    def save_game(self, game: QuizGame) -> bool:
        pass
