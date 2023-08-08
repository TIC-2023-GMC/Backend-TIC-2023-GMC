from bson import ObjectId
import inject
from src.Photo.Domain.Photo import Photo
from src.Photo.Domain.PhotoFactory import PhotoFactory
from src.Photo.Domain.PhotoRepository import PhotoRepository


class SavePhotoUseCase:
    @inject.autoparams()
    def __init__(self, photo_repository: PhotoRepository):
        self.photo_repository = photo_repository

    def execute_user(self, img, user_id) -> str:
        return self.photo_repository.save_photo_user(img=img, user_id=user_id)

    def execute_pub(self, img) -> Photo:
        photo_url = self.photo_repository.upload_img(img)
        photo = PhotoFactory.create(photo_url)
        return photo
