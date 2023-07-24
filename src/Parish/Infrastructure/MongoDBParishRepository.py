from pymongo import MongoClient
import os
from dotenv import load_dotenv

from src.Parish.Domain.ParishRepository import ParishRepository

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


class MongoDBParishRepository(ParishRepository):
    def get_all(self):
        parishes_collection = db["parishes"]
        parishes_data = parishes_collection.find()
        parishes_list = [
            {"label": parish["label"], "value": parish["value"]}
            for parish in parishes_data
        ]
        return parishes_list
