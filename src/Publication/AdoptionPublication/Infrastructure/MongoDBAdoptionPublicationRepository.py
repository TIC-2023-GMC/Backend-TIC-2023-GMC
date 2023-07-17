from Publication.AdoptionPublication.Domain.AdoptionPublicationFactory import (
    AdoptionPublicationFactory,
)
from Publication.Domain.PublicationRepository import PublicationRepository
from pymongo import MongoClient
from bson import ObjectId

client = MongoClient(
    "mongodb://admin:password123@localhost:27017/pawqdb?authSource=admin"
)
db = client["pawqdb"]

adoption_publications = db["adoption_publications"]
experience_publications = db["experience_publications"]


class MongoDBAdoptionPublicationRepository(PublicationRepository):
    def add_publication(self, publication):
        publication_dict = publication.dict()
        publication_dict["_id"] = ObjectId()

        adoption_publications.insert_one(publication_dict)

    def get_all(self, pageNumber, pageSize):
        skip_count = (pageNumber - 1) * pageSize
        documents = adoption_publications.find({}).skip(skip_count).limit(pageSize)

        publication_list = [
            AdoptionPublicationFactory.createPublication(**doc) for doc in documents
        ]

        return publication_list, pageNumber + 1

    def get_by_id(self, id):
        document = adoption_publications.find_one({"_id": id})
        return document

    def get_by_filters(self, species, date, location, pageNumber, pageSize):
        filters = {}
        if species:
            filters["species"] = species
        if date:
            filters["publication_date"] = {"$gte": date.strftime("%Y-%m-%d")}
        if location:
            filters["pet_location"] = location

        skip_count = (pageNumber - 1) * pageSize
        documents = adoption_publications.find(filters).skip(skip_count).limit(pageSize)

        publication_list = [
            AdoptionPublicationFactory.createPublication(**doc) for doc in documents
        ]

        return publication_list, pageNumber + 1

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
