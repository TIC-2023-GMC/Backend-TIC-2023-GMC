from abc import ABC, abstractmethod
from typing import List

from src.Interaction.Like.Domain.Like import Like
class LikeRepository(ABC):
    @abstractmethod
    def add_like_adoption_pub(self, pub_id: str, user_id:str) -> Like:
        pass
    def remove_like_by_id(self, like_id: str) -> None:
        pass
    def get_likes_by_pub_id(self, like_id: str) -> List[Like]:
        pass
