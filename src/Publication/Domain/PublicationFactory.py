from abc import ABC, abstractmethod
from src.Publication.Domain.Publication import Publication


class PublicationFactory(ABC):
    @abstractmethod
    def create_publication(self) -> Publication:
        pass
