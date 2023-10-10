from typing import List

from src.Match.Domain.Match import Match
from src.Match.WordSearchGameMatch.Domain.Topic.Topic import Topic


class WordSearchGameMatch(Match):
    match_game_topic: Topic
