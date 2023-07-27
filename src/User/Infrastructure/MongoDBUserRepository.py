from bson import ObjectId
from src.Interaction.Comment.Domain.CommentFactory import CommentFactory
from src.Interaction.Like.Domain.LikeFactory import LikeFactory
from src.Photo.Domain.PhotoFactory import PhotoFactory
from src.User.Domain.UserFactory import UserFactory
from src.Publication.AdoptionPublication.Domain.AdoptionPublicationFactory import (
    AdoptionPublicationFactory,
)
from src.Publication.AdoptionPublication.Domain.AdoptionPublication import (
    AdoptionPublication,
)
from src.Shared.MongoClient import MongoDBConnection
from src.User.Domain.UserRepository import UserRepository
from typing import List


class MongoDBUserRepository(UserRepository):
    db = MongoDBConnection().get_db()
    adoption_publications = db["adoption_publications"]
    users = db["users"]

    def add_user(self, user):
        user_dict = user.dict()
        return self.users.insert_one(user_dict)

    def get_user(self, email, password):
        return self.users.find_one({"email": email, "password": password})

    def get_by_id(self, id):
        return self.users.find_one({"_id": id})

    def update_user(self, updated_user):
        return self.users.update_one(
            {"_id": updated_user._id}, {"$set": updated_user.dict()}
        )

    def add_favorite_pub(self, pub):
        return self.users.update_one(
            {"_id": pub.user_id}, {"$push": {"favorite_publications": pub._id}}
        )

    def remove_favorite_pub(self, pub):
        return self.users.update_one(
            {"_id": pub.user_id}, {"$pull": {"favorite_publications": pub._id}}
        )

    def list_favorite_publications(
        self, favorite_adoption_publications: List[str]
    ) -> List[AdoptionPublication]:
        favorite_adoption_publications = [
            ObjectId(id) for id in favorite_adoption_publications
        ]
        documents = self.adoption_publications.find(
            {"_id": {"$in": favorite_adoption_publications}}
        )
        favorites_list = []
        for doc in documents:
            doc["_id"] = str(doc["_id"])
            user = UserFactory.create(**doc["user"])
            user._id = str(user._id)
            photo = PhotoFactory.create(**doc["photo"])
            photo._id = str(photo._id)
            likes = []
            for like in doc["likes"]:
                like_obj = LikeFactory.create(**like)
                like_obj._id = str(like._id)
                likes.append(like_obj)
            comments = []
            for comment in doc["comments"]:
                comment_obj = CommentFactory.create(**comment)
                comment_obj._id = str(like._id)
                comments.append(comment_obj)
            publication = AdoptionPublicationFactory.create_publication(**doc)
            publication.user = user
            publication.photo = photo
            publication.likes = likes
            publication.comments = comments
            favorites_list.append(publication)

        return favorites_list
