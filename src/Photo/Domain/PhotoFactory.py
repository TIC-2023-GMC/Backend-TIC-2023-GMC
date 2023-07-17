from src.Photo.Domain.Photo import Photo


class PhotoFactory:
    def create(_id: str, img_path: str) -> Photo:
        return Photo(_id=_id, img_path=img_path)
