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


class MongoDBConnection:
    def __init__(self):
        self.client = MongoClient(mongo_uri)
        self.db = self.client[mongo_database]
        self.adoption_publications = self.db["adoption_publications"]
        self.experience_publications = self.db["experience_publications"]

    def get_db(self):
        return self.db


class MongoDBConnectionSingleton:
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            # Inicializa la conexión a la base de datos
            cls.__instance.connection = MongoDBConnection()
        return cls.__instance

    def get_db(self):
        return self.connection.get_db()


# Uso del Singleton para obtener la conexión a la base de datos
mongo_client_singleton = MongoDBConnectionSingleton()
db = mongo_client_singleton.get_db()
