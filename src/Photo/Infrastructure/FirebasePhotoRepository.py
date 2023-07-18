from src.Photo.Domain.PhotoRepository import PhotoRepository
from src.Photo.Infrastructure.firebase.firebase_config import initialize_firebase
from firebase_admin import storage
from src.Photo.Domain.Photo import Photo

firebase_app = initialize_firebase()


class FirebasePhotoRepository(PhotoRepository):
    def get_by_id(self, id: str):
        pass

    """ def upload_img(self, img) -> str:
        bucket = storage.bucket(app=firebase_app)
        blob = bucket.blob(img.filename)
        blob.upload_from_file(img.file)
        url = blob.public_url
        return url """

    def upload_img(self, img) -> str:
        bucket = storage.bucket(app=firebase_app)
        blob = bucket.blob(img.filename)
        blob.upload_from_file(img.file)
        url = f"https://firebasestorage.googleapis.com/v0/b/{bucket.name}/o/{blob.name}?alt=media"
        return url

    def save_photo_user(self, photo: Photo, user_id: str):
        pass
