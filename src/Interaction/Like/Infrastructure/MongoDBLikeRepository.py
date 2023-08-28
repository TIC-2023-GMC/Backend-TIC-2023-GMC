from bson import ObjectId
from src.Interaction.Like.Domain.LikeRepository import LikeRepository
from src.Shared.MongoClient import MongoDBConnection


class MongoDBLikeRepository(LikeRepository):
    db = MongoDBConnection().get_db()
    adoption_publications = db["adoption_publications"]
    users = db["users"]

    def add_like_adoption_pub(self, pub_id: str, user_id: str) -> None:
        pub_id = ObjectId(pub_id)
        user_id = ObjectId(user_id)
        if user_id in self.adoption_publications.find_one({"_id": pub_id}).get(
            "likes", []
        ):
            raise Exception("ya existe el like")
        return self.adoption_publications.update_one(
            {"_id": pub_id}, {"$push": {"likes": user_id}}
        )
        
    