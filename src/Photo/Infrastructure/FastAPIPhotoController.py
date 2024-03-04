from fastapi import APIRouter, File, HTTPException, UploadFile

from src.Photo.Application.SavePhotoUseCase import SavePhotoUseCase
from src.Photo.Domain.Photo import Photo
from src.Shared.Singleton import singleton

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
def upload_photo(photo: UploadFile = File(...)) -> Photo:
    try:
        return get_adoption_controller().save_pub_photo_endpoint(photo)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
