from src.Publication.AdoptionPublication.Domain.AdoptionPublication import (
    AdoptionPublication,
)
from src.Publication.AdoptionPublication.Domain.AdoptionPublicationFactory import (
    AdoptionPublicationFactory,
)
from src.Publication.Domain.PublicationRepository import PublicationRepository
from bson import ObjectId
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
adoption_publications = db["adoption_publications"]
experience_publications = db["experience_publications"]


class MongoDBAdoptionPublicationRepository(PublicationRepository):
    def add_publication(self, publication: AdoptionPublication):
        publication_dict = publication.dict()
        publication_dict["_id"] = ObjectId()
        adoption_publications.insert_one(publication_dict)

    def get_by_id(self, id):
        document = adoption_publications.find_one({"_id": id})
        return document

    def get_all(self, species, date, location, page_number, page_size):
        filters = {}
        if species:
            filters["species"] = species
        if date:
            filters["publication_date"] = {"$gte": date}
        if location:
            filters["pet_location"] = location

        skip_count = (page_number - 1) * page_size
        documents = (
            adoption_publications.find(filters).skip(skip_count).limit(page_size)
        )

        publication_list = []
        for doc in documents:
            doc["_id"] = str(doc["_id"])
            publication = AdoptionPublicationFactory.create_publication(**doc)
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
