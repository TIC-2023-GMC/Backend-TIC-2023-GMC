from src.Shared.MongoClient import MongoDBConnection
from src.Parish.Domain.ParishRepository import ParishRepository


class MongoDBParishRepository(ParishRepository):
    db = MongoDBConnection().get_db()
    parishes_collection = db["parishes"]

    def get_all(self):
        parishes_data = self.parishes_collection.find()
        parishes_list = [
            {"label": parish["label"], "value": parish["value"]}
            for parish in parishes_data
        ]
        return parishes_list
