import inject

from src.Match.QuizGameMatch.Domain.QuizGameMatch import QuizGameMatch
from src.Match.QuizGameMatch.Domain.QuizGameMatchRepository import (
    QuizGameMatchRepository,
)


class GetQuizGameMatchUseCase:
    @inject.autoparams()
    def __init__(self, repository: QuizGameMatchRepository):
        self.repository = repository

    def execute(self, user_id: str) -> QuizGameMatch:
        return self.repository.get_match(user_id=user_id)
