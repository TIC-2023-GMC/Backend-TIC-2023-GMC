import inject
from src.Game.QuizGame.Domain.QuizGame import QuizGame
from src.Game.QuizGame.Domain.QuizGameRepository import QuizGameRepository


class SaveQuizGameUseCase:
    @inject.autoparams()
    def __init__(self, repository: QuizGameRepository):
        self.repository = repository

    def execute(self, new_quiz_game: QuizGame) -> bool:
        return self.repository.save_game(game=new_quiz_game)
