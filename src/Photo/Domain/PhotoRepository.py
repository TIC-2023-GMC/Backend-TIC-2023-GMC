from abc import ABC, abstractmethod

from src.Photo.Domain.Photo import Photo


class PhotoRepository(ABC):
    @abstractmethod
    def get_by_id(self, id: str):
        pass

    @abstractmethod
    def upload_img(self, img):
        pass

    @abstractmethod
    def save_photo_user(self, photo: Photo, user_id: str):
        pass

    @abstractmethod
    def save_photo_pub(self, photo: Photo, pub_id: str):
        pass
