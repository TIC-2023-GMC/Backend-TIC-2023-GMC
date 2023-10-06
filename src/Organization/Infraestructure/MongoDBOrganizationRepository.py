from typing import List, Tuple
from src.Organization.Domain.Organization import Organization
from src.Organization.Domain.OrganizationFactory import OrganizationFactory
from src.Organization.Domain.OrganizationRepository import OrganizationRepository
from src.Photo.Domain.PhotoFactory import PhotoFactory
from src.Shared.MongoClient import MongoDBConnection


class MongoDBOrganizationRepository(OrganizationRepository):
    db = MongoDBConnection().get_db()
    organization_collection = db["organizations"]

    def get_all(
        self, page_number: int, page_size: int
    ) -> Tuple[List[Organization], int]:
        skip_count = (page_number - 1) * page_size
        documents = (
            self.organization_collection.find()
            .sort([("organization_name", 1)])
            .skip(skip_count)
            .limit(page_size)
        )
        organization_list = []
        for doc in documents:
            doc["_id"] = str(doc["_id"])
            photo = PhotoFactory.create(**doc["organization_photo"])
            organization = OrganizationFactory.create_organization(**doc)
            organization.organization_photo = photo
            organization_list.append(organization)
        return organization_list, page_number
