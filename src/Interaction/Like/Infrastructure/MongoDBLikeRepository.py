from bson import ObjectId
from src.Interaction.Like.Domain.LikeRepository import LikeRepository
from src.Shared.MongoClient import MongoDBConnection


class MongoDBLikeRepository(LikeRepository):
    db = MongoDBConnection().get_db()
    adoption_publications = db["adoption_publications"]
    experience_publications = db["experience_publications"]
    users = db["users"]

    def add_like(self, pub_id: str, user_id: str, is_adoption: bool) -> None:
        pub_id = ObjectId(pub_id)
        user_id = ObjectId(user_id)

        if is_adoption:
            collection = self.adoption_publications
            publication = self.adoption_publications.find_one({"_id": pub_id})
        else:
            collection = self.experience_publications
            publication = self.experience_publications.find_one({"_id": pub_id})

        if publication:
            likes = publication.get("likes", [])
            if user_id in map(ObjectId, likes):
                raise Exception("Ya existe el like")
            return collection.update_one({"_id": pub_id}, {"$push": {"likes": user_id}})
        raise Exception("No existe la publicación")

    def remove_like(self, pub_id: str, user_id: str, is_adoption: bool) -> None:
        pub_id = ObjectId(pub_id)
        user_id = ObjectId(user_id)

        if is_adoption:
            collection = self.adoption_publications
            publication = self.adoption_publications.find_one({"_id": pub_id})
        else:
            collection = self.experience_publications
            publication = self.experience_publications.find_one({"_id": pub_id})
        if publication:
            likes = publication.get("likes", [])
            if user_id not in map(ObjectId, likes):
                raise Exception("El like no existe")
            return collection.update_one({"_id": pub_id}, {"$pull": {"likes": user_id}})
        raise Exception("No existe la publicación")
