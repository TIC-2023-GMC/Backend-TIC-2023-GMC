from typing import List, Tuple

from bson import ObjectId

from src.Interaction.Like.Domain.LikeFactory import LikeFactory
from src.Photo.Domain.PhotoFactory import PhotoFactory
from src.Publication.Domain.PublicationRepository import PublicationRepository
from src.Publication.ExperiencePublication.Domain.ExperiencePublication import (
    ExperiencePublication,
)
from src.Publication.ExperiencePublication.Domain.ExperiencePublicationFactory import (
    ExperiencePublicationFactory,
)
from src.Shared.MongoClient import MongoDBConnection
from src.User.Domain.UserFactory import UserFactory


class MongoDBExperiencePublicationRepository(PublicationRepository):
    db = MongoDBConnection().get_db()
    experience_publications = db["experience_publications"]

    def add_publication(self, publication: ExperiencePublication) -> None:
        publication.user._id = ObjectId(publication.user._id)
        publication_dict = publication.dict()
        publication_dict["_id"] = ObjectId()
        self.experience_publications.insert_one(publication_dict)

    def get_by_id(self, id) -> ExperiencePublication:
        document = self.experience_publications.find_one({"_id": ObjectId(id)})
        return document

    def get_all(
        self, species, date, page_number, page_size
    ) -> Tuple[List[ExperiencePublication], int]:
        filters = {}
        if species:
            filters["species"] = species
        if date:
            filters["publication_date"] = {"$gte": date}

        skip_count = (page_number - 1) * page_size
        documents = (
            self.experience_publications.find(filters)
            .sort([("publication_date", -1), ("_id", -1)])
            .skip(skip_count)
            .limit(page_size)
        )

        publication_list = []
        for doc in documents:
            doc["_id"] = str(doc["_id"])
            user = UserFactory.create(**doc["user"])
            user._id = str(user._id)
            photo = PhotoFactory.create(**doc["photo"])
            likes_object_ids = doc["likes"]
            doc["likes"] = [LikeFactory.create(str(like)) for like in likes_object_ids]
            publication = ExperiencePublicationFactory.create_publication(**doc)
            publication.user = user
            publication.photo = photo
            publication_list.append(publication)

        return publication_list, page_number + 1

    def add_like(self, pub_id: str, user_id: str) -> None:
        pub_id = ObjectId(pub_id)
        user_id = ObjectId(user_id)
        collection = self.experience_publications
        publication = self.experience_publications.find_one({"_id": pub_id})
        if publication:
            likes = publication.get("likes", [])
            if user_id in map(ObjectId, likes):
                raise Exception("Ya existe el like")
            return collection.update_one({"_id": pub_id}, {"$push": {"likes": user_id}})
        raise Exception("No existe la publicación")

    def remove_like(self, pub_id: str, user_id: str) -> None:
        pub_id = ObjectId(pub_id)
        user_id = ObjectId(user_id)
        collection = self.experience_publications
        publication = self.experience_publications.find_one({"_id": pub_id})
        if publication:
            likes = publication.get("likes", [])
            if user_id not in map(ObjectId, likes):
                raise Exception("El like no existe")
            return collection.update_one({"_id": pub_id}, {"$pull": {"likes": user_id}})
        raise Exception("No existe la publicación")
