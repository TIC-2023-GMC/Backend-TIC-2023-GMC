from abc import ABC, abstractmethod

from src.Match.WordleGameMatch.Domain.WordleMatch import WordleMatch


class WordleMatchRepository(ABC):
    @abstractmethod
    def get_match(self, user_id: str) -> WordleMatch:
        pass

    @abstractmethod
    def save_match(self, match: WordleMatch) -> bool:
        pass
