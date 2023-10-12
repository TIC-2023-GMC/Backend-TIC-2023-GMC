from src.Match.Domain.MatchFactory import MatchFactory
from src.Match.WordSearchGameMatch.Domain.Topic.Topic import Topic
from src.Match.WordSearchGameMatch.Domain.WordSearchGameMatch import WordSearchGameMatch


class WordSearchGameMatchFactory(MatchFactory):
    @staticmethod
    def create_game(
        _id: str,
        user_id: str,
        match_name: str,
        match_game_onboarding: str,
        match_game_topic: Topic,
    ) -> WordSearchGameMatch:
        return WordSearchGameMatch(
            _id=_id,
            user_id=user_id,
            match_name=match_name,
            match_game_score=0,
            match_game_time=0,
            match_game_onboarding=match_game_onboarding,
            match_game_topic=match_game_topic,
        )
