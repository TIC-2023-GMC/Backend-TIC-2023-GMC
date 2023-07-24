from src.Shared.MongoClient import MongoDBConnectionSingleton

from src.Parish.Domain.ParishRepository import ParishRepository

mongo_client_singleton = MongoDBConnectionSingleton()
db = mongo_client_singleton.get_db()


class MongoDBParishRepository(ParishRepository):
    def get_all(self):
        parishes_collection = db["parishes"]
        parishes_data = parishes_collection.find()
        parishes_list = [
            {"label": parish["label"], "value": parish["value"]}
            for parish in parishes_data
        ]
        return parishes_list
