import os
from pymongo import MongoClient

# MongoDB connection details
mongodb_host = "localhost"
mongodb_port = 27017
"""
mongodb_username = '${MONGO_INITDB_ROOT_USERNAME}'
mongodb_password = '${MONGO_INITDB_ROOT_PASSWORD}'
mongodb_database = '${MONGO_INITDB_DATABASE}'
"""
mongodb_username = os.environ["MONGO_INITDB_ROOT_USERNAME"]
mongodb_password = os.environ["MONGO_INITDB_ROOT_PASSWORD"]
mongodb_database = os.environ["MONGO_INITDB_DATABASE"]

# Connect to MongoDB
client = MongoClient(
    host=mongodb_host,
    port=mongodb_port,
    username=mongodb_username,
    password=mongodb_password,
)
db = client[mongodb_database]

# Insert initial data
users_collection = db["users"]
users_data = {
    "first_name": "Gandhy",
    "last_name": "García",
    "mobile_phone": "0983473043",
    "neighborhood": "Cumbayá",
    "email": "gandhygarcia@outlook.es",
    "password": "password123",
    "num_previous_pets": 2,
    "num_current_pets": 1,
    "outdoor_hours": 6,
    "house_space": 100,
    "has_yard": False,
    "main_pet_food": "Casera",
    "pet_expenses": 40.5,
    "motivation": "Amor por los animales",
    "favorite_adoption_publications": [],
    "photo": {
        "_id": 2,
        "img_path": "https://scontent.fgye1-1.fna.fbcdn.net/v/t1.6435-9/74242360_3195954163812838_4274861617784553472_n.jpg?_nc_cat=110&ccb=1-7&_nc_sid=09cbfe&_nc_eui2=AeFRCjYsTZuQlf2PHyTPJ3HYymegSJbxrSjKZ6BIlvGtKPYIzlm5LEqBr9cR0tDl-FEvtHfkBqZQ6LHCgw-pkTlW&_nc_ohc=dye6H3TWD6QAX-v2xOF&_nc_ht=scontent.fgye1-1.fna&oh=00_AfCF85oDfvg1CEtIJ1We_mJ3gV49fRwyklxfDfl8SouHOA&oe=64D84DE2",
    },
}

users_collection.insert_one(users_data)

adoption_publications_collection = db["adoption_publications"]

adoption_publications_data = [
    {
        "user": {
            "first_name": "Gandhy",
            "last_name": "García",
            "mobile_phone": "0983473043",
            "neighborhood": "Cumbayá",
            "email": "gandhygarcia@outlook.es",
            "password": "password123",
            "num_previous_pets": 2,
            "num_current_pets": 1,
            "outdoor_hours": 6,
            "house_space": 100,
            "has_yard": False,
            "main_pet_food": "Casera",
            "pet_expenses": 40.5,
            "motivation": "Amor por los animales",
            "favorite_adoption_publications": [],
            "photo": {
                "photo_id": 2,
                "img_path": "https://scontent.fgye1-1.fna.fbcdn.net/v/t1.6435-9/74242360_3195954163812838_4274861617784553472_n.jpg?_nc_cat=110&ccb=1-7&_nc_sid=09cbfe&_nc_eui2=AeFRCjYsTZuQlf2PHyTPJ3HYymegSJbxrSjKZ6BIlvGtKPYIzlm5LEqBr9cR0tDl-FEvtHfkBqZQ6LHCgw-pkTlW&_nc_ohc=dye6H3TWD6QAX-v2xOF&_nc_ht=scontent.fgye1-1.fna&oh=00_AfCF85oDfvg1CEtIJ1We_mJ3gV49fRwyklxfDfl8SouHOA&oe=64D84DE2",
            },
        },
        "description": "Hermoso gato de 3 meses busca un hogar",
        "publication_date": "2023-07-13",
        "photo": {
            "_id": 1,
            "img_path": "https://scontent.fgye1-1.fna.fbcdn.net/v/t1.18169-9/536695_10200665558588650_1941658362_n.jpg?_nc_cat=106&ccb=1-7&_nc_sid=cdbe9c&_nc_eui2=AeH1q50jt5HgoS9npXdWLf1o3gXquT50xBLeBeq5PnTEEljZbDM758A0rOfiYECvjiE8vlhQ-yUUmKdFdDU59f_k&_nc_ohc=oR1QzT31QVUAX8xTWNQ&_nc_ht=scontent.fgye1-1.fna&oh=00_AfCapPgF09isXflAy1ql9TSyfw4rVU30HvueR9hG4xp3jA&oe=64D90FB8",
        },
        "likes": [],
        "comments": [],
        "species": "Gato",
        "pet_size": "Pequeño",
        "pet_breed": "Montés",
        "pet_age": 0.25,
        "pet_sex": True,  # boolean -> True: Male, False: Female
        "pet_location": "Cumbayá",
        "sterilized": True,
        "vaccination_card": False,
    },
    {
        "user": {
            "first_name": "Gandhy",
            "last_name": "García",
            "mobile_phone": "0983473043",
            "neighborhood": "Cumbayá",
            "email": "gandhygarcia@outlook.es",
            "password": "password123",
            "num_previous_pets": 2,
            "num_current_pets": 1,
            "outdoor_hours": 6,
            "house_space": 100,
            "has_yard": False,
            "main_pet_food": "Casera",
            "pet_expenses": 40.5,
            "motivation": "Amor por los animales",
            "favorite_adoption_publications": [],
            "photo": {
                "photo_id": 2,
                "img_path": "https://scontent.fgye1-1.fna.fbcdn.net/v/t1.6435-9/74242360_3195954163812838_4274861617784553472_n.jpg?_nc_cat=110&ccb=1-7&_nc_sid=09cbfe&_nc_eui2=AeFRCjYsTZuQlf2PHyTPJ3HYymegSJbxrSjKZ6BIlvGtKPYIzlm5LEqBr9cR0tDl-FEvtHfkBqZQ6LHCgw-pkTlW&_nc_ohc=dye6H3TWD6QAX-v2xOF&_nc_ht=scontent.fgye1-1.fna&oh=00_AfCF85oDfvg1CEtIJ1We_mJ3gV49fRwyklxfDfl8SouHOA&oe=64D84DE2",
            },
        },
        "description": "Perrita de 1 año busca un hogar",
        "publication_date": "2023-07-14",
        "photo": {
            "_id": 3,
            "img_path": "https://scontent.fgye1-1.fna.fbcdn.net/v/t1.18169-9/536695_10200665558588650_1941658362_n.jpg?_nc_cat=106&ccb=1-7&_nc_sid=cdbe9c&_nc_eui2=AeH1q50jt5HgoS9npXdWLf1o3gXquT50xBLeBeq5PnTEEljZbDM758A0rOfiYECvjiE8vlhQ-yUUmKdFdDU59f_k&_nc_ohc=oR1QzT31QVUAX8xTWNQ&_nc_ht=scontent.fgye1-1.fna&oh=00_AfCapPgF09isXflAy1ql9TSyfw4rVU30HvueR9hG4xp3jA&oe=64D90FB8",
        },
        "likes": [],
        "comments": [],
        "species": "Perro",
        "pet_size": "Mediano",
        "pet_breed": "Mestizo",
        "pet_age": 1,
        "pet_sex": False,  # boolean -> True: Male, False: Female
        "pet_location": "Solanda",
        "sterilized": False,
        "vaccination_card": False,
    },
]
adoption_publications_collection.insert_many(adoption_publications_data)

organizations_collection = db["organizations"]
organizations_data = [
    {
        "name": "Unidad de Bienestar Animal",
        "address": "Quito",
        "website": "www.facebook.com",
    },
    {"name": "PARE", "address": "Tumbaco", "website": "www.youtube.com"},
]
organizations_collection.insert_many(organizations_data)


# Close the MongoDB connection
client.close()
