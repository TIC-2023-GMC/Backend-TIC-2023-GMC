from Photo.Domain.Photo import Photo


class PhotoFactory:
    def create(photo_id: int, img_path: str) -> Photo:
        return Photo(photo_id=photo_id, img_path=img_path)
