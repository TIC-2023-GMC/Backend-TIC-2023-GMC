from src.Photo.Domain.PhotoRepository import PhotoRepository


class SavePhotoUseCase:
    def __init__(self, photo_repository: PhotoRepository):
        self.photo_repository = photo_repository

    def execute_user(self, img, user_id):
        return self.photo_repository.save_photo_user(img=img, user_id=user_id)

    def execute_pub(self, img, pub_id):
        return self.photo_repository.save_photo_pub(img=img, pub_id=pub_id)
