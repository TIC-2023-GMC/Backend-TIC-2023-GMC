import inject
from src.Match.WordleGameMatch.Domain.WordleMatch import WordleMatch

from src.Match.WordleGameMatch.Domain.WordleMatchRepository import WordleMatchRepository


class SaveWordleMatchUseCase:
    @inject.autoparams()
    def __init__(self, repository: WordleMatchRepository):
        self.repository = repository

    def execute(self, match: WordleMatch) -> bool:
        return self.repository.save_match(match=match)
