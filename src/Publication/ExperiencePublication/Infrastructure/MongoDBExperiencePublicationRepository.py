from typing import List, Tuple
from src.Interaction.Comment.Domain.Comment import Comment
from src.Interaction.Like.Domain.Like import Like
from src.Shared.MongoClient import MongoDBConnection
from src.Publication.ExperiencePublication.Domain.ExperiencePublicationFactory import (
    ExperiencePublicationFactory,
)
from src.Publication.ExperiencePublication.Domain.ExperiencePublication import (
    ExperiencePublication,
)
from src.Interaction.Comment.Domain.CommentFactory import CommentFactory
from src.Interaction.Like.Domain.LikeFactory import LikeFactory
from src.Photo.Domain.PhotoFactory import PhotoFactory
from src.User.Domain.UserFactory import UserFactory
from src.Publication.Domain.PublicationRepository import PublicationRepository
from bson import ObjectId
from typing import List, Tuple


class MongoDBExperiencePublicationRepository(PublicationRepository):
    db = MongoDBConnection().get_db()
    experience_publications = db["experience_publications"]

    def add_publication(self, publication: ExperiencePublication) -> None:
        publication.user._id = ObjectId(publication.user._id)
        publication_dict = publication.dict()
        publication_dict["_id"] = ObjectId()
        self.experience_publications.insert_one(publication_dict)

    def get_by_id(self, id) -> ExperiencePublication:
        pass

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
            likes = []
            for like in doc["likes"]:
                like_obj = LikeFactory.create(**like)
                like_obj._id = str(like._id)
                likes.append(like_obj)
            for comment in doc["comments"]:
                comment._id = str(comment._id)
            publication = ExperiencePublicationFactory.create_publication(**doc)
            publication.user = user
            publication.photo = photo
            publication.likes = likes
            publication.comments = doc["comments"]
            publication_list.append(publication)

        return publication_list, page_number + 1

    def add_like(self, like) -> None:
        # Implement the logic for adding a like to a publication in MongoDB
        pass

    def remove_like_by_id(self, like_id) -> None:
        # Implement the logic for removing a like by ID from MongoDB
        pass

    def get_likes_by_pub_id(self, id) -> List[Like]:
        # Implement the logic for getting likes by publication ID from MongoDB
        pass
