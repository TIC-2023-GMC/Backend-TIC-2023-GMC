from abc import ABC
from src.Organization.Domain.Organization import Organization
from src.Organization.Domain.SocialMedia import SocialMedia
from src.Photo.Domain.Photo import Photo


class OrganizationFactory(ABC):
    @staticmethod
    def create_organization(
        _id: str,
        organization_name: str,
        organization_description: str,
        organization_photo: Photo,
        external_links: SocialMedia,
    ) -> Organization:
        return Organization(
            _id=_id,
            organization_name=organization_name,
            organization_description=organization_description,
            organization_photo=organization_photo,
            external_links=external_links,
        )
