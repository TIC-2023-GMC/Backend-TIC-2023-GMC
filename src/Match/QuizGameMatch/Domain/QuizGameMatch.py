from typing import List
from src.Match.Domain.Match import Match
from src.Match.QuizGameMatch.Domain.Question.Question import Question


class QuizGameMatch(Match):
    match_game_questions: List[Question]
