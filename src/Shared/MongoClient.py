from pymongo import MongoClient
import os
from dotenv import load_dotenv

from src.Shared.Singleton import singleton

load_dotenv()
mongo_url = os.getenv("MONGO_URL")
mongo_port = os.getenv("MONGO_PORT")
mongo_user = os.getenv("MONGOUSER")
mongo_password = os.getenv("MONGOPASSWORD")
mongo_database = os.getenv("MONGO_INITDB_DATABASE")
mongo_uri = f"mongodb://{mongo_user}:{mongo_password}@{mongo_url}:{mongo_port}/?authMechanism=DEFAULT"


@singleton
class MongoDBConnection:
    def __init__(self):
        self.client = MongoClient(mongo_uri)
        self.db = self.client[mongo_database]

    def get_db(self):
        return self.db
