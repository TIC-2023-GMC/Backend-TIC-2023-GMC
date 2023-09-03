from datetime import datetime
from src.Interaction.Comment.Domain.CommentRepository import CommentRepository
from src.Interaction.Comment.Domain.Comment import Comment
from src.Shared.MongoClient import MongoDBConnection
from src.Interaction.Comment.Domain.CommentFactory import CommentFactory
from src.Publication.Domain.PublicationRepository import PublicationRepository
from bson import ObjectId
from typing import List, Tuple


class MongoDBCommentRepository(CommentRepository):
    db = MongoDBConnection().get_db()
    comments = db["comments"]
    adoption_publications = db["adoption_publications"]
    experience_publications = db["experience_publications"]

    def add_comment(
        self,
        pub_id: str,
        user_id: str,
        comment_text: str,
        is_adoption: bool,
    ) -> None:
        user_id = ObjectId(user_id)
        user = self.db["users"].find_one({"_id": user_id})
        if not user:
            raise Exception("No existe el usuario")
        user_first_name = user["first_name"]
        user_last_name = user["last_name"]
        user_photo = user["photo"]
        _id = None
        comment_date = datetime.now()
        comment = CommentFactory.create(
            _id,
            user_first_name,
            user_last_name,
            comment_text,
            comment_date,
            user_photo,
            str(user_id),
        )
        comment_dict = comment.dict()
        comment_dict["_id"] = ObjectId()
        comment_dict["user_id"] = ObjectId(comment_dict["user_id"])
        self.comments.insert_one(comment_dict)
        pub_id = ObjectId(pub_id)
        if is_adoption:
            collection = self.adoption_publications
            publication = self.adoption_publications.find_one({"_id": pub_id})
        else:
            collection = self.experience_publications
            publication = self.experience_publications.find_one({"_id": pub_id})
        if publication:
            return collection.update_one(
                {"_id": pub_id}, {"$push": {"comments": comment_dict["_id"]}}
            )
        raise Exception("No existe la publicación")

    def update_comment(self, comment_id: str, comment_text: str) -> None:
        comment_id = ObjectId(comment_id)
        comment = self.comments.find_one({"_id": comment_id})
        print(comment)
        new_date = datetime.now()
        print(new_date)
        if not comment:
            raise Exception("No existe el comentario")
        return self.comments.update_one(
            {"_id": comment_id},
            {"$set": {"comment_text": comment_text, "comment_date": new_date}},
        )

    def get_comments_by_id(
        self, comments_id: List[str], page_number: int, page_size: int
    ) -> Comment:
        skip_count = (page_number - 1) * page_size
        comments_id = [ObjectId(id) for id in comments_id]
        documents = (
            self.comments.find({"_id": {"$in": comments_id}})
            .sort([("publication_date", -1), ("_id", -1)])
            .skip(skip_count)
            .limit(page_size)
        )
        comments = []
        for doc in documents:
            doc["_id"] = str(doc["_id"])
            doc["user_id"] = str(doc["user_id"])
            comment = CommentFactory.create(**doc)
            comments.append(comment)
        return comments, page_number + 1
