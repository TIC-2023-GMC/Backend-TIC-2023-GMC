from fastapi import APIRouter, UploadFile, File
from src.Shared.Singleton import singleton
from src.Photo.Domain.Photo import Photo
from src.Photo.Application.SavePhotoUseCase import SavePhotoUseCase

router = APIRouter()


@singleton
class FastAPIPhotoController:
    def __init__(self):
        self.save_photo = SavePhotoUseCase()

    def save_user_photo_endpoint(self, img, user_id):
        pass

    def save_pub_photo_endpoint(self, photo_file: UploadFile) -> Photo:
        photo = self.save_photo.execute_pub(photo_file)
        return photo


def get_adoption_controller() -> FastAPIPhotoController:
    return FastAPIPhotoController()


@router.post("/upload", status_code=201)
def upload_photo(photo: UploadFile = File(...)) -> None:
    return get_adoption_controller().save_pub_photo_endpoint(photo)
