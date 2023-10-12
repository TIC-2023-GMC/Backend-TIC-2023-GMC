from typing import List
from src.Match.Domain.Match import Match
from src.Match.Domain.MatchFactory import MatchFactory
from src.Match.WordleGameMatch.Domain.WordleMatch import WordleMatch


class WordleMatchFactory(MatchFactory):
    @staticmethod
    def create_game(
        _id: str,
        user_id: str,
        match_name: str,
        match_game_score: int,
        match_game_time: int,
        match_game_onboarding: str,
        wordle_game_clue: str,
        wordle_game_description: str,
        wordle_game_words: List[str],
    ) -> WordleMatch:
        return WordleMatch(
            _id=_id,
            user_id=user_id,
            match_name=match_name,
            match_game_score=match_game_score,
            match_game_time=match_game_time,
            match_game_onboarding=match_game_onboarding,
            wordle_game_clue=wordle_game_clue,
            wordle_game_description=wordle_game_description,
            wordle_game_words=wordle_game_words,
        )
