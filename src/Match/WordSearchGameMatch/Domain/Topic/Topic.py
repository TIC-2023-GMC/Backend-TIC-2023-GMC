from typing import List
from src.Match.WordSearchGameMatch.Domain.Statement.Statement import Statement

from src.Shared.Model import Model


class Topic(Model):
    info: str
    statements: List[Statement]
