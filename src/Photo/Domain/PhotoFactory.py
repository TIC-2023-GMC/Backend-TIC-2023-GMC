from src.Photo.Domain.Photo import Photo


class PhotoFactory:
    @staticmethod
    def create(img_path: str) -> Photo:
        return Photo(img_path=img_path)
