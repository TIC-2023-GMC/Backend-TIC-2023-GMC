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
    comments = db["publication_comments"]

    def add_comment(
        self, pub_id: str, user_id: str, comment_text: str, comment_date: datetime
    ) -> None:
        user_id = ObjectId(user_id)
        user = self.db["users"].find_one({"_id": user_id})
        if not user:
            raise Exception("No existe el usuario")
        user_first_name = user["first_name"]
        user_last_name = user["last_name"]
        user_photo = user["photo"]
        _id = None
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

        pub_id = ObjectId(pub_id)
        comments_document = self.comments.find_one({"_id": pub_id})

        if comments_document:
            return self.comments.update_one(
                {"_id": pub_id}, {"$push": {"comments": comment_dict}}
            )
        else:
            return self.comments.insert_one({"_id": pub_id, "comments": [comment_dict]})

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

    def delete_comment(self, pub_id: str, comment_id: str) -> None:
        pub_id = ObjectId(pub_id)
        comments_document = self.comments.find_one({"_id": pub_id})
        if comments_document:
            if len(comments_document["comments"]) == 0:
                raise Exception("La publicación no tiene comentarios")
            else:
                return self.comments.update_one(
                    {"_id": pub_id},
                    {"$pull": {"comments": {"_id": ObjectId(comment_id)}}},
                )
        else:
            raise Exception("La publicación no tiene comentarios")

    def get_comments_by_id(
        self, pub_id: str, page_number: int, page_size: int
    ) -> Tuple[List[Comment], int]:
        pub_id = ObjectId(pub_id)
        document = self.comments.find_one({"_id": pub_id})

        if document:
            publication_comments = document.get("comments", [])
            publication_comments.sort(key=lambda x: x["comment_date"], reverse=True)
            skip_count = (page_number - 1) * page_size
            start_index = skip_count
            end_index = skip_count + page_size
            paginated_comments = publication_comments[start_index:end_index]

            comments = []

            for doc in paginated_comments:
                doc["_id"] = str(doc["_id"])
                doc["user_id"] = str(doc["user_id"])
                comment = CommentFactory.create(**doc)
                comments.append(comment)
            return comments, page_number + 1
        else:
            return [], page_number + 1
