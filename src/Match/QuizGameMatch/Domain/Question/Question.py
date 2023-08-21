from typing import List
from src.Match.QuizGameMatch.Domain.Answer.Answer import Answer
from src.Shared.Model import Model


class Question(Model):
    question_text: str
    answers: List[Answer]
