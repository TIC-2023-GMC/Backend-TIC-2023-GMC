from abc import ABC, abstractmethod

from src.Interaction.Domain.Interaction import Interaction


class InteractionFactory(ABC):
    @abstractmethod
    def create(self) -> Interaction:
        pass
