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
from pymongo import MongoClient
import os
from dotenv import load_dotenv


load_dotenv()
mongo_url = os.getenv("MONGO_URL")
mongo_port = os.getenv("MONGO_PORT")
mongo_user = os.getenv("MONGOUSER")
mongo_password = os.getenv("MONGOPASSWORD")
mongo_database = os.getenv("MONGO_INITDB_DATABASE")

# Crea la cadena de conexión utilizando las variables de entorno
mongo_uri = f"mongodb://{mongo_user}:{mongo_password}@{mongo_url}:{mongo_port}/?authMechanism=DEFAULT"

# Crea el cliente de MongoDB
client = MongoClient(mongo_uri)
# Accede a la base de datos deseada
db = client[mongo_database]

experience_publications = db["experience_publications"]


class MongoDBExperiencePublicationRepository(PublicationRepository):
    def add_publication(self, publication: ExperiencePublication):
        pass

    def get_by_id(self, id):
        pass

    def get_all(self, species, date, page_number, page_size):
        filters = {}
        if species:
            filters["species"] = species
        if date:
            filters["publication_date"] = {"$gte": date}
        print(
            species,
            date,
            page_number,
            page_size
        )
        skip_count = (page_number - 1) * page_size
        documents = (
            experience_publications.find(filters)
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
            publication = ExperiencePublicationFactory.create_publication(**doc)
            publication.user = user
            publication.photo = photo
            publication.likes = likes
            publication.comments = comments
            publication_list.append(publication)
        return publication_list, page_number + 1

    def add_like(self, like):
        # Implement the logic for adding a like to a publication in MongoDB
        pass

    def remove_like_by_id(self, like_id):
        # Implement the logic for removing a like by ID from MongoDB
        pass

    def get_likes_by_pub_id(self, id):
        # Implement the logic for getting likes by publication ID from MongoDB
        pass

    def get_comments_by_pub_id(self, id):
        # Implement the logic for getting comments by publication ID from MongoDB
        pass

    def add_comment(self, comment):
        # Implement the logic for adding a comment to a publication in MongoDB
        pass
