from abc import ABC, abstractmethod


class PublicationRepository(ABC):
    @abstractmethod
    def add_publication(self, publication):
        pass

    @abstractmethod
    def get_all(self, pageNumber, pageSize):
        pass

    @abstractmethod
    def get_by_id(self, id):
        pass

    @abstractmethod
    def get_by_filters(self, species, date, location):
        pass

    @abstractmethod
    def add_like(self, like):
        pass

    @abstractmethod
    def remove_like_by_id(self, like_id):
        pass

    @abstractmethod
    def get_likes_by_pub_id(self, id):
        pass

    @abstractmethod
    def get_comments_by_pub_id(self, id):
        pass

    @abstractmethod
    def add_comment(self, comment):
        pass
