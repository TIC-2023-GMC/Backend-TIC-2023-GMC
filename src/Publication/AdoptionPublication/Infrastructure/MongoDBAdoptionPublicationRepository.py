from typing import List, Tuple

from bson import ObjectId

from src.Interaction.Comment.Domain.Comment import Comment
from src.Interaction.Comment.Domain.CommentFactory import CommentFactory
from src.Interaction.Like.Domain.Like import Like
from src.Interaction.Like.Domain.LikeFactory import LikeFactory
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
        publication.user._id = ObjectId(publication.user._id)
        publication_dict = publication.dict()
        publication_dict["_id"] = ObjectId()
        self.adoption_publications.insert_one(publication_dict)

    def get_by_id(self, id) -> AdoptionPublication:
        document = self.adoption_publications.find_one({"_id": ObjectId(id)})
        return document

    def get_all(
        self, species, date, location, page_number, page_size
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
            user = UserFactory.create(**doc["user"])
            user._id = str(user._id)
            photo = PhotoFactory.create(**doc["photo"])
            likes_object_ids = doc["likes"]
            doc["likes"] = [LikeFactory.create(str(like)) for like in likes_object_ids]
            publication = AdoptionPublicationFactory.create_publication(**doc)
            publication.user = user
            publication.photo = photo
            publication_list.append(publication)

        return publication_list, page_number + 1
