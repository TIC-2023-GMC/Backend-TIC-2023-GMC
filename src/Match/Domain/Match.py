from typing import Optional
from src.Shared.Model import Model


class Match(Model):
    _id: Optional[str]
    user_id: str
    match_name: str
    match_game_score: int
    match_game_time: int
    match_game_onboarding: str
