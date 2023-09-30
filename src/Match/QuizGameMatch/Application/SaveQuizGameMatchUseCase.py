import inject

from src.Match.QuizGameMatch.Domain.QuizGameMatch import QuizGameMatch
from src.Match.QuizGameMatch.Domain.QuizGameMatchRepository import (
    QuizGameMatchRepository,
)


class SaveQuizGameMatchUseCase:
    @inject.autoparams()
    def __init__(self, repository: QuizGameMatchRepository):
        self.repository = repository

    def execute(self, new_quiz_match: QuizGameMatch) -> bool:
        return self.repository.save_match(match=new_quiz_match)
