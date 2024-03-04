from typing import List
from src.Match.Domain.MatchFactory import MatchFactory
from src.Match.QuizGameMatch.Domain.Question.Question import Question
from src.Match.QuizGameMatch.Domain.QuizGameMatch import QuizGameMatch


class QuizGameMatchFactory(MatchFactory):
    @staticmethod
    def create_game(
        _id: str,
        user_id: str,
        match_name: str,
        match_game_score: int,
        match_game_time: int,
        match_game_onboarding: str,
        match_game_questions: List[Question],
    ) -> QuizGameMatch:
        return QuizGameMatch(
            _id=_id,
            user_id=user_id,
            match_name=match_name,
            match_game_score=match_game_score,
            match_game_time=match_game_time,
            match_game_onboarding=match_game_onboarding,
            match_game_questions=match_game_questions,
        )
