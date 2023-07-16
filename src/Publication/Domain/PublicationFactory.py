from abc import ABC, abstractmethod
from Publication.Domain.Publication import Publication


class PublicationFactory(ABC):
    @abstractmethod
    def createPublication(self) -> Publication:
        pass
