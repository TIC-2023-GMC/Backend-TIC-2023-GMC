from typing import List
from src.Game.QuizGame.Domain.Answer import Answer

from src.Shared.Model import Model


class Question(Model):
    question_text: str
    answers: List[Answer]
