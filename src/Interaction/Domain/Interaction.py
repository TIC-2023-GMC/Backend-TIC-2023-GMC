from abc import ABC
from Shared.Model import Model
from User.Domain.User import User


class Interaction(Model, ABC):
    user: User
