from abc import abstractmethod, ABC

from src.Match.WordSearchGameMatch.Domain.WordSearchGameMatch import WordSearchGameMatch


class WordSearchGameMatchRepository(ABC):
    @abstractmethod
    def get_match(self, user_id: str) -> WordSearchGameMatch:
        pass
