from typing import List
from src.Match.WordSearchGameMatch.Domain.Statement.Statement import Statement

from src.Shared.Model import Model


class Topic(Model):
    title: str
    info: str
    statements: List[Statement]
