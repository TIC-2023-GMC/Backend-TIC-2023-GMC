from typing import List, Tuple

from bson import ObjectId

from src.Interaction.Comment.Domain.CommentFactory import CommentFactory
from src.Interaction.Like.Domain.LikeFactory import LikeFactory
from src.Photo.Domain.PhotoFactory import PhotoFactory
from src.Publication.AdoptionPublication.Domain.AdoptionPublication import (
    AdoptionPublication,
)
from src.Publication.AdoptionPublication.Domain.AdoptionPublicationFactory import (
    AdoptionPublicationFactory,
)
from src.Shared.MongoClient import MongoDBConnection
from src.User.Domain.User import User
from src.User.Domain.UserFactory import UserFactory
from src.User.Domain.UserRepository import UserRepository


class MongoDBUserRepository(UserRepository):
    db = MongoDBConnection().get_db()
    adoption_publications = db["adoption_publications"]
    users = db["users"]
    user_favorite_publications = db["user_favorite_publications"]

    def add_user(self, user: User) -> None:
        user_dict = user.dict()
        return self.users.insert_one(user_dict)

    def get_user(self, email, password) -> User:
        return self.users.find_one({"email": email, "password": password})

    def get_by_id(self, _id: str) -> User:
        doc = self.users.find_one({"_id": ObjectId(_id)})
        doc["_id"] = str(doc["_id"])
        user_favorites = self.user_favorite_publications.find_one(
            {"_id": ObjectId(_id)}
        )
        if user_favorites:
            user_favorites["favorite_adoption_publications"] = [
                str(id) for id in user_favorites["favorite_adoption_publications"]
            ]
            doc["favorite_adoption_publications"] = user_favorites[
                "favorite_adoption_publications"
            ]
        else:
            doc["favorite_adoption_publications"] = []
        user = UserFactory.create(**doc)
        return user

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
        user_favorites = self.user_favorite_publications.find_one({"_id": user_id})
        if user_favorites is None or pub_id not in user_favorites.get(
            "favorite_adoption_publications", []
        ):
            return self.user_favorite_publications.update_one(
                {"_id": user_id},
                {"$push": {"favorite_adoption_publications": pub_id}},
                upsert=True,
            )
        raise Exception("ya existe la publicación en la lista de favoritos")

    def remove_favorite_pub(self, pub_id: str, user_id: str) -> None:
        pub_id = ObjectId(pub_id)
        user_id = ObjectId(user_id)
        user_favorites = self.user_favorite_publications.find_one({"_id": user_id})
        if user_favorites and pub_id in user_favorites.get(
            "favorite_adoption_publications", []
        ):
            return self.user_favorite_publications.update_one(
                {"_id": user_id}, {"$pull": {"favorite_adoption_publications": pub_id}}
            )
        raise Exception("No se elimino la publicación en la lista de favoritos")

    def list_favorite_publications(
        self,
        user_id: str,
        page_number: int,
        page_size: int,
    ) -> Tuple[List[AdoptionPublication], int]:
        skip_count = (page_number - 1) * page_size
        favorites = self.user_favorite_publications.find_one({"_id": ObjectId(user_id)})
        if not favorites:
            return [], page_number
        else:
            documents = (
                self.adoption_publications.find(
                    {"_id": {"$in": favorites["favorite_adoption_publications"]}}
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
                likes_object_ids = doc["likes"]
                doc["likes"] = [
                    LikeFactory.create(str(like)) for like in likes_object_ids
                ]
                object_ids = doc["comments"]
                doc["comments"] = [str(object_id) for object_id in object_ids]
                publication = AdoptionPublicationFactory.create_publication(**doc)
                publication.user = user
                publication.photo = photo
                favorites_list.append(publication)

            return favorites_list, page_number + 1

    def list_my_publications(
        self, page_number: int, page_size: int, user_id: str
    ) -> Tuple[List[AdoptionPublication], int]:
        skip_count = (page_number - 1) * page_size

        documents = (
            self.adoption_publications.find({"user._id": ObjectId(user_id)})
            .sort([("publication_date", -1), ("_id", -1)])
            .skip(skip_count)
            .limit(page_size)
        )

        publications_list = []
        for doc in documents:
            doc["_id"] = str(doc["_id"])
            user = UserFactory.create(**doc["user"])
            user._id = str(user._id)
            photo = PhotoFactory.create(**doc["photo"])
            likes_object_ids = doc["likes"]
            doc["likes"] = [LikeFactory.create(str(like)) for like in likes_object_ids]
            object_ids = doc["comments"]
            doc["comments"] = [str(object_id) for object_id in object_ids]
            publication = AdoptionPublicationFactory.create_publication(**doc)
            publication.user = user
            publication.photo = photo
            publications_list.append(publication)

        return publications_list, page_number + 1
