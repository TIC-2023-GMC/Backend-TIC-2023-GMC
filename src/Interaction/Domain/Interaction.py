from abc import ABC

from src.Shared.Model import Model


class Interaction(Model, ABC):
    user_id: str
