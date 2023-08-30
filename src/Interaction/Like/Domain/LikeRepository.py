from abc import ABC, abstractmethod
from typing import List

from src.Interaction.Like.Domain.Like import Like


class LikeRepository(ABC):
    @abstractmethod
    def add_like(self, pub_id: str, user_id: str, is_adoption: bool) -> None:
        pass

    def remove_like(self, user_id: str, pub_id: str, is_adoption: bool) -> None:
        pass
