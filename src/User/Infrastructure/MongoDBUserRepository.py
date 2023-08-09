from bson import ObjectId
from src.User.Domain.User import User
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
from typing import List, Tuple


class MongoDBUserRepository(UserRepository):
    db = MongoDBConnection().get_db()
    adoption_publications = db["adoption_publications"]
    users = db["users"]

    def add_user(self, user: User) -> None:
        user_dict = user.dict()
        return self.users.insert_one(user_dict)

    def get_user(self, email, password) -> User:
        return self.users.find_one({"email": email, "password": password})

    def get_by_id(self, id: float) -> User:
        return self.users.find_one({"_id": id})

    def update_user(self, updated_user: User) -> None:
        updated_user = updated_user.dict()
        updated_user["_id"] = ObjectId(updated_user["_id"])
        attributes_to_remove = ["password", "email", "favorite_adoption_publications"]
        for attribute in attributes_to_remove:
            updated_user.pop(attribute, None)
        return self.users.update_one(
            {"_id": updated_user["_id"]}, {"$set": updated_user}
        )

    def add_favorite_pub(self, pub_id: str, user_id: str) -> None:
        pub_id = ObjectId(pub_id)
        user_id = ObjectId(user_id)
        if pub_id in self.users.find_one({"_id": user_id}).get(
            "favorite_adoption_publications", []
        ):
            raise Exception("ya existe la publicación en la lista de favoritos")
        return self.users.update_one(
            {"_id": user_id}, {"$push": {"favorite_adoption_publications": pub_id}}
        )

    def remove_favorite_pub(self, pub_id: str, user_id: str) -> None:
        pub_id = ObjectId(pub_id)
        user_id = ObjectId(user_id)
        if pub_id not in self.users.find_one({"_id": user_id}).get(
            "favorite_adoption_publications", []
        ):
            raise Exception("No se encontro la publicación en la lista de favoritos")
        return self.users.update_one(
            {"_id": user_id}, {"$pull": {"favorite_adoption_publications": pub_id}}
        )

    def list_favorite_publications(
        self,
        favorite_adoption_publications: List[str],
        page_number: int,
        page_size: int,
    ) -> Tuple[List[AdoptionPublication], int]:
        skip_count = (page_number - 1) * page_size
        favorite_adoption_publications = [
            ObjectId(id) for id in favorite_adoption_publications
        ]
        documents = (
            self.adoption_publications.find(
                {"_id": {"$in": favorite_adoption_publications}}
            )
            .sort([("publication_date", -1), ("_id", -1)])
            .skip(skip_count)
            .limit(page_size)
        )
        favorites_list = []
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

        return favorites_list, page_number + 1
