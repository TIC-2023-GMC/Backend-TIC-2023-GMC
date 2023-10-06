
from src.Organization.Domain.SocialMedia import SocialMedia
from src.Photo.Domain.Photo import Photo
from src.Shared.Model import Model


class Organization(Model):
    _id: str
    organization_name: str
    organization_description: str
    organization_photo: Photo
    external_links: SocialMedia
