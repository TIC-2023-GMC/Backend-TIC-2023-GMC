from src.Photo.Domain.PhotoRepository import PhotoRepository
from src.Photo.Infrastructure.firebase.firebase_config import initialize_firebase
from src.Photo.Domain.Photo import Photo


class FirebasePhotoRepository(PhotoRepository):
    firebase_storage = initialize_firebase()

    def get_by_id(self, id: str):
        pass

    def upload_img(self, img) -> str:
        response = self.firebase_storage.child(img.filename).put(img.file)
        url = self.firebase_storage.child(img.filename).get_url(
            response["downloadTokens"]
        )
        return url

    def save_photo_user(self, photo: Photo, user_id: str):
        pass
