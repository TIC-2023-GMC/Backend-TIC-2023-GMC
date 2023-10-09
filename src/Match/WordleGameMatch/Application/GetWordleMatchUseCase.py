import inject
from src.Match.WordleGameMatch.Domain.WordleMatch import WordleMatch

from src.Match.WordleGameMatch.Domain.WordleMatchRepository import WordleMatchRepository


class GetWordleMatchUseCase:
    @inject.autoparams()
    def __init__(self, repository: WordleMatchRepository):
        self.repository = repository
    
    def execute(self, user_id: str)-> WordleMatch:
        return self.repository.get_match(user_id=user_id)
    