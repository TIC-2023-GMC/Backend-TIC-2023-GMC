import inject

from src.Match.WordSearchGameMatch.Domain.WordSearchGameMatch import WordSearchGameMatch
from src.Match.WordSearchGameMatch.Domain.WordSearchGameMatchRepository import (
    WordSearchGameMatchRepository,
)


class WordSearchGameMatchUseCase:
    @inject.autoparams()
    def __init__(self, repository: WordSearchGameMatchRepository):
        self.repository = repository

    def execute(self, user_id: str) -> WordSearchGameMatch:
        return self.repository.get_match(user_id=user_id)
