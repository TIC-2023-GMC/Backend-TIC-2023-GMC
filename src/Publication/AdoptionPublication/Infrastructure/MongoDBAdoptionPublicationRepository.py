import datetime
from typing import List, Tuple

from bson import ObjectId

from src.Photo.Domain.PhotoFactory import PhotoFactory
from src.Publication.AdoptionPublication.Domain.AdoptionPublication import (
    AdoptionPublication,
)
from src.Publication.AdoptionPublication.Domain.AdoptionPublicationFactory import (
    AdoptionPublicationFactory,
)
from src.Publication.Domain.PublicationRepository import PublicationRepository
from src.Shared.MongoClient import MongoDBConnection
from src.User.Domain.UserFactory import UserFactory


class MongoDBAdoptionPublicationRepository(PublicationRepository):
    db = MongoDBConnection().get_db()
    adoption_publications = db["adoption_publications"]

    def add_publication(self, publication: AdoptionPublication) -> None:
        publication.user.id = ObjectId(publication.user.id)
        publication_dict = publication.dict()
        publication_dict["_id"] = ObjectId()
        self.adoption_publications.insert_one(publication_dict)

    def get_by_id(self, _id: str) -> AdoptionPublication:
        document = self.adoption_publications.find_one({"_id": ObjectId(_id)})
        return document

    def get_all(
        self,
        user_id: str,
        species: str,
        date: datetime,
        location: str,
        page_number: int,
        page_size: int,
    ) -> Tuple[List[AdoptionPublication], int]:
        filters = {}
        if species:
            filters["species"] = species
        if date:
            filters["publication_date"] = {"$gte": date}
        if location:
            filters["pet_location"] = location

        skip_count = (page_number - 1) * page_size
        documents = (
            self.adoption_publications.find(filters)
            .sort([("publication_date", -1), ("_id", -1)])
            .skip(skip_count)
            .limit(page_size)
        )

        publication_list = []
        for doc in documents:
            doc["_id"] = str(doc["_id"])
            doc["user"]["_id"] = str(doc["user"]["_id"])
            user = UserFactory.create(**doc["user"])
            photo = PhotoFactory.create(**doc["photo"])
            likes_object_ids = doc["likes"]
            doc["likes"] = (
                len(likes_object_ids),
                ObjectId(user_id) in likes_object_ids,
            )
            doc["is_favorite"] = False
            publication = AdoptionPublicationFactory.create_publication(**doc)
            publication.user = user
            publication.photo = photo
            publication_list.append(publication)

        return publication_list, page_number + 1

    def add_like(self, pub_id: str, user_id: str) -> None:
        pub_id = ObjectId(pub_id)
        user_id = ObjectId(user_id)
        collection = self.adoption_publications
        publication = self.adoption_publications.find_one({"_id": pub_id})
        if publication:
            likes = publication.get("likes", [])
            if user_id in map(ObjectId, likes):
                raise Exception("Ya existe el like")
            return collection.update_one({"_id": pub_id}, {"$push": {"likes": user_id}})
        raise Exception("No existe la publicación")

    def remove_like(self, pub_id: str, user_id: str) -> None:
        pub_id = ObjectId(pub_id)
        user_id = ObjectId(user_id)
        collection = self.adoption_publications
        publication = self.adoption_publications.find_one({"_id": pub_id})
        if publication:
            likes = publication.get("likes", [])
            if user_id not in map(ObjectId, likes):
                raise Exception("El like no existe")
            return collection.update_one({"_id": pub_id}, {"$pull": {"likes": user_id}})
        raise Exception("No existe la publicación")
