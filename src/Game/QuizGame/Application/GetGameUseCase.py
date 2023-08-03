import inject
from src.Game.QuizGame.Domain.QuizGameRepository import QuizGameRepository

from src.Game.QuizGame.Domain.QuizGame import QuizGame


class GetQuizGameUseCase:
    @inject.autoparams()
    def __init__(self, repository: QuizGameRepository):
        self.repository = repository

    def execute(self, user_id: str) -> QuizGame:
        return self.repository.get_game(user_id=user_id)
