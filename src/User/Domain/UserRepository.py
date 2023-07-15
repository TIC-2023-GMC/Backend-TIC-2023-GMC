from abc import ABC, abstractmethod


class UserRepository(ABC):
    @abstractmethod
    def add_user(self, user):
        pass

    @abstractmethod
    def get_user(self, email, password):
        pass

    @abstractmethod
    def update_user(self, updated_user):
        pass

    @abstractmethod
    def get_by_id(self, id):
        pass

    @abstractmethod
    def add_favorite_pub(self, pub):
        pass

    @abstractmethod
    def remove_favorite_pub(self, pub):
        pass

    @abstractmethod
    def list_favorite_publications(self, user):
        pass
