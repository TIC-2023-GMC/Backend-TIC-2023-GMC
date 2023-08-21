from abc import ABC
from src.Shared.Model import Model
from src.User.Domain.User import User


class Interaction(Model, ABC):
    user_id: str
