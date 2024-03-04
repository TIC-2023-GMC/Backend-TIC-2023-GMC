from abc import ABC, abstractmethod
from typing import List

from src.Parish.Domain.Parish import Parish


class ParishRepository(ABC):
    @abstractmethod
    def get_all(self) -> List[Parish]:
        pass
