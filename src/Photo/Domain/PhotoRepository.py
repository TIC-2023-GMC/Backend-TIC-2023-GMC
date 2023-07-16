from abc import ABC, abstractmethod


class PhotoRepository(ABC):
    @abstractmethod
    def get_by_id(self, id):
        pass

    @abstractmethod
    def upload_img(self, img):
        pass

    @abstractmethod
    def save_photo_user(self, photo, user_id):
        pass

    @abstractmethod
    def save_photo_pub(self, photo, pub_id):
        pass
