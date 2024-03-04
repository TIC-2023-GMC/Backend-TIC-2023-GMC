from abc import ABC, abstractmethod

from src.Photo.Domain.Photo import Photo


class PhotoRepository(ABC):
    @abstractmethod
    def get_by_id(self, id: str) -> Photo:
        pass

    @abstractmethod
    def upload_img(self, img) -> str:
        pass

    @abstractmethod
    def save_photo_user(self, photo: Photo, user_id: str) -> str:
        pass
