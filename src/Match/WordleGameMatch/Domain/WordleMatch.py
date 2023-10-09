from typing import List
from src.Match.Domain.Match import Match

class WordleMatch(Match):
    wordle_game_clue: str
    wordle_game_description: str
    wordle_game_words: List[str]
