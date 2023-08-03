import datetime
import os
from bson import ObjectId
from pymongo import MongoClient

# MongoDB connection details
mongodb_host = "localhost"
mongodb_port = 27017
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

# Users
users_collection = db["users"]
users_data = {
    "_id": ObjectId("64c1b0ef0fd89c04b7114eb7"),
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
    "main_pet_food": "homemade",
    "pet_expenses": 40.5,
    "motivation": "Love for animals",
    "favorite_adoption_publications": [],
    "photo": {
        "_id": 2,
        "img_path": "https://scontent.fgye1-1.fna.fbcdn.net/v/t1.6435-9/74242360_3195954163812838_4274861617784553472_n.jpg?_nc_cat=110&ccb=1-7&_nc_sid=09cbfe&_nc_eui2=AeFRCjYsTZuQlf2PHyTPJ3HYymegSJbxrSjKZ6BIlvGtKPYIzlm5LEqBr9cR0tDl-FEvtHfkBqZQ6LHCgw-pkTlW&_nc_ohc=dye6H3TWD6QAX-v2xOF&_nc_ht=scontent.fgye1-1.fna&oh=00_AfCF85oDfvg1CEtIJ1We_mJ3gV49fRwyklxfDfl8SouHOA&oe=64D84DE2",
    },
}
users_collection.insert_one(users_data)
user = users_collection.find_one({"email": "gandhygarcia@outlook.es"})

# Adoption publications
adoption_publications_collection = db["adoption_publications"]
adoption_publications_data = [
    {
        "user": user,
        "description": "Hermoso gato de 3 meses busca un hogar",
        "publication_date": datetime.datetime.now(),
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
        "user": user,
        "description": "Perrita de 1 año busca un hogar",
        "publication_date": datetime.datetime.now(),
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

# Experience publications
experience_publications_collection = db["experience_publications"]
experience_publications_data = [
    {
        "user": user,
        "description": "Mi gatito lo conoci en la calle",
        "publication_date": datetime.datetime.now(),
        "photo": {
            "_id": 1,
            "img_path": "https://scontent.fgye1-1.fna.fbcdn.net/v/t1.18169-9/536695_10200665558588650_1941658362_n.jpg?_nc_cat=106&ccb=1-7&_nc_sid=cdbe9c&_nc_eui2=AeH1q50jt5HgoS9npXdWLf1o3gXquT50xBLeBeq5PnTEEljZbDM758A0rOfiYECvjiE8vlhQ-yUUmKdFdDU59f_k&_nc_ohc=oR1QzT31QVUAX8xTWNQ&_nc_ht=scontent.fgye1-1.fna&oh=00_AfCapPgF09isXflAy1ql9TSyfw4rVU30HvueR9hG4xp3jA&oe=64D90FB8",
        },
        "likes": [],
        "comments": [],
        "species": "Gato",
    },
    {
        "user": user,
        "description": "Perrita de 1 año busca un hogar",
        "publication_date": datetime.datetime.now(),
        "photo": {
            "_id": 3,
            "img_path": "https://scontent.fgye1-1.fna.fbcdn.net/v/t1.18169-9/536695_10200665558588650_1941658362_n.jpg?_nc_cat=106&ccb=1-7&_nc_sid=cdbe9c&_nc_eui2=AeH1q50jt5HgoS9npXdWLf1o3gXquT50xBLeBeq5PnTEEljZbDM758A0rOfiYECvjiE8vlhQ-yUUmKdFdDU59f_k&_nc_ohc=oR1QzT31QVUAX8xTWNQ&_nc_ht=scontent.fgye1-1.fna&oh=00_AfCapPgF09isXflAy1ql9TSyfw4rVU30HvueR9hG4xp3jA&oe=64D90FB8",
        },
        "likes": [],
        "comments": [],
        "species": "Perro",
    },
]
experience_publications_collection.insert_many(experience_publications_data)

# Organizations
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

# Parishes
parishes_collection = db["parishes"]
parishes_data = [
    {"label": "BELISARIO QUEVEDO", "value": "BELISARIO QUEVEDO"},
    {"label": "CARCELÉN", "value": "CARCELÉN"},
    {"label": "CENTRO HISTÓRICO", "value": "CENTRO HISTÓRICO"},
    {"label": "COCHAPAMBA", "value": "COCHAPAMBA"},
    {"label": "COMITÉ DEL PUEBLO", "value": "COMITÉ DEL PUEBLO"},
    {"label": "COTOCOLLAO", "value": "COTOCOLLAO"},
    {"label": "CHILIBULO", "value": "CHILIBULO"},
    {"label": "CHILLOGALLO", "value": "CHILLOGALLO"},
    {"label": "CHIMBACALLE", "value": "CHIMBACALLE"},
    {"label": "EL CONDADO", "value": "EL CONDADO"},
    {"label": "GUAMANÍ", "value": "GUAMANÍ"},
    {"label": "IÑAQUITO", "value": "IÑAQUITO"},
    {"label": "ITCHIMBÍA", "value": "ITCHIMBÍA"},
    {"label": "JIPIJAPA", "value": "JIPIJAPA"},
    {"label": "KENNEDY", "value": "KENNEDY"},
    {"label": "LA ARGELIA", "value": "LA ARGELIA"},
    {"label": "LA CONCEPCIÓN", "value": "LA CONCEPCIÓN"},
    {"label": "LA ECUATORIANA", "value": "LA ECUATORIANA"},
    {"label": "LA FERROVIARIA", "value": "LA FERROVIARIA"},
    {"label": "LA LIBERTAD", "value": "LA LIBERTAD"},
    {"label": "LA MAGDALENA", "value": "LA MAGDALENA"},
    {"label": "LA MENA", "value": "LA MENA"},
    {"label": "MARISCAL SUCRE", "value": "MARISCAL SUCRE"},
    {"label": "PONCEANO", "value": "PONCEANO"},
    {"label": "PUENGASÍ", "value": "PUENGASÍ"},
    {"label": "QUITUMBE", "value": "QUITUMBE"},
    {"label": "RUMIPAMBA", "value": "RUMIPAMBA"},
    {"label": "SAN BARTOLO", "value": "SAN BARTOLO"},
    {"label": "SAN ISIDRO DEL INCA", "value": "SAN ISIDRO DEL INCA"},
    {"label": "SAN JUAN", "value": "SAN JUAN"},
    {"label": "SOLANDA", "value": "SOLANDA"},
    {"label": "TURUBAMBA", "value": "TURUBAMBA"},
    {
        "label": "QUITO DISTRITO METROPOLITANO",
        "value": "QUITO DISTRITO METROPOLITANO",
    },
    {"label": "ALANGASÍ", "value": "ALANGASÍ"},
    {"label": "AMAGUAÑA", "value": "AMAGUAÑA"},
    {"label": "ATAHUALPA", "value": "ATAHUALPA"},
    {"label": "CALACALÍ", "value": "CALACALÍ"},
    {"label": "CALDERÓN", "value": "CALDERÓN"},
    {"label": "CONOCOTO", "value": "CONOCOTO"},
    {"label": "CUMBAYÁ", "value": "CUMBAYÁ"},
    {"label": "CHAVEZPAMBA", "value": "CHAVEZPAMBA"},
    {"label": "CHECA", "value": "CHECA"},
    {"label": "EL QUINCHE", "value": "EL QUINCHE"},
    {"label": "GUALEA", "value": "GUALEA"},
    {"label": "GUANGOPOLO", "value": "GUANGOPOLO"},
    {"label": "GUAYLLABAMBA", "value": "GUAYLLABAMBA"},
    {"label": "LA MERCED", "value": "LA MERCED"},
    {"label": "LLANO CHICO", "value": "LLANO CHICO"},
    {"label": "LLOA", "value": "LLOA"},
    {"label": "MINDO", "value": "MINDO"},
    {"label": "NANEGAL", "value": "NANEGAL"},
    {"label": "NANEGALITO", "value": "NANEGALITO"},
    {"label": "NAYÓN", "value": "NAYÓN"},
    {"label": "NONO", "value": "NONO"},
    {"label": "PACTO", "value": "PACTO"},
    {"label": "PEDRO VICENTE MALDONADO", "value": "PEDRO VICENTE MALDONADO"},
    {"label": "PERUCHO", "value": "PERUCHO"},
    {"label": "PIFO", "value": "PIFO"},
    {"label": "PÍNTAG", "value": "PÍNTAG"},
    {"label": "POMASQUI", "value": "POMASQUI"},
    {"label": "PUÉLLARO", "value": "PUÉLLARO"},
    {"label": "PUEMBO", "value": "PUEMBO"},
    {"label": "SAN ANTONIO", "value": "SAN ANTONIO"},
    {"label": "SAN JOSÉ DE MINAS", "value": "SAN JOSÉ DE MINAS"},
    {"label": "SAN MIGUEL DE LOS BANCOS", "value": "SAN MIGUEL DE LOS BANCOS"},
    {"label": "TABABELA", "value": "TABABELA"},
    {"label": "TUMBACO", "value": "TUMBACO"},
    {"label": "YARUQUÍ", "value": "YARUQUÍ"},
    {"label": "ZAMBIZA", "value": "ZAMBIZA"},
    {"label": "PUERTO QUITO", "value": "PUERTO QUITO"},
]
parishes_collection.insert_many(parishes_data)

# Game Quiz
game_quiz_collection = db["game_quiz"]
game_quiz_data = [
    {
        "user_id": ObjectId("64c1b0ef0fd89c04b7114eb7"),
        "game_name": "Quiz 1",
        "game_description": "This is a Test Quiz",
        "game_image": {"img_path": "string"},
        "game_category": "string",
        "game_score": 0,
        "game_questions": [],
        "game_time": 0,
    }
]
game_quiz_collection.insert_many(game_quiz_data)

# Questions
questions_collection = db["questions_quiz"]
questions_data = [
    {
        "question_text": "¿Qué se considera una infracción según el Artículo 120?",
        "answers": [
            {
                "answer_text": "Un acto que cumple con las disposiciones.",
                "is_correct": False,
            },
            {
                "answer_text": "Un acto que no afecta a la fauna urbana.",
                "is_correct": False,
            },
            {
                "answer_text": "Un acto u omisión que incumple con las disposiciones y afecta a la fauna urbana.",
                "is_correct": True,
            },
        ],
    },
    {
        "question_text": "¿Cómo se dividen las infracciones en el artículo 120?",
        "answers": [
            {
                "answer_text": "Leves y graves.",
                "is_correct": False,
            },
            {
                "answer_text": "Graves y muy graves.",
                "is_correct": False,
            },
            {
                "answer_text": "Leves, graves y muy graves.",
                "is_correct": True,
            },
        ],
    },
    {
        "question_text": "¿Cuál de las siguientes acciones se considera una infracción leve?",
        "answers": [
            {
                "answer_text": "No cumplir con el calendario de vacunas y desparasitación.",
                "is_correct": True,
            },
            {
                "answer_text": "No mantener a los animales dentro de los predios privados, permitiendo que deambulen por el espacio público sin supervisión.",
                "is_correct": False,
            },
            {
                "answer_text": "Perder el carnet de vacunación del animal.",
                "is_correct": False,
            },
            {
                "answer_text": "No socializar a los animales con otros perros.",
                "is_correct": False,
            },
        ],
    },
    {
        "question_text": "¿Cuál es la sanción para las infracciones leves según el artículo 121?",
        "answers": [
            {
                "answer_text": "Multa del 30% de una remuneración básica unificada.",
                "is_correct": True,
            },
            {
                "answer_text": "Servicio comunitario por 48 horas.",
                "is_correct": False,
            },
            {
                "answer_text": "Multa del 10% de una remuneración básica unificada.",
                "is_correct": False,
            },
            {
                "answer_text": "Suspensión temporal de la tenencia de mascotas.",
                "is_correct": False,
            },
        ],
    },
    {
        "question_text": "Las sanciones que se mencionan en el artículo 121, ¿Tienen tienen perjuicio penal?",
        "answers": [
            {
                "answer_text": "Si",
                "is_correct": False,
            },
            {
                "answer_text": "No",
                "is_correct": True,
            },
        ],
    },
    {
        "question_text": "Las sanciones que se mencionan en el artículo 121, ¿Tienen tienen perjuicio Civil?",
        "answers": [
            {
                "answer_text": "Si",
                "is_correct": False,
            },
            {
                "answer_text": "No",
                "is_correct": True,
            },
        ],
    },
    {
        "question_text": "¿Cuál de las siguientes acciones se considera una infracción leve?",
        "answers": [
            {
                "answer_text": "Permitir que deambulen por las vías sin collar.",
                "is_correct": True,
            },
            {
                "answer_text": "No mantener a los animales dentro de los predios privados, permitiendo que deambulen por el espacio público sin la supervisión.",
                "is_correct": False,
            },
            {
                "answer_text": "Perder el carnet de vacunación del animal.",
                "is_correct": False,
            },
            {
                "answer_text": "Socializar a los animales con otros animales de compañia.",
                "is_correct": False,
            },
        ],
    },
    {
        "question_text": "¿Cuál de las siguientes acciones se considera una infracción leve?",
        "answers": [
            {
                "answer_text": "Recoger excrementos del animal de compañía en espacios públicos o privados.",
                "is_correct": False,
            },
            {
                "answer_text": "No recoger excrementos del animal de compañía en espacios públicos o privados.",
                "is_correct": True,
            },
            {
                "answer_text": "Baños al animal de compañía por la noche.",
                "is_correct": False,
            },
            {
                "answer_text": "Recoger el excremento del animal de compañía.",
                "is_correct": False,
            },
        ],
    },
    {
        "question_text": "Bañar a un animal de compañía en noche, ¿Se considera una infracción?",
        "answers": [
            {
                "answer_text": "Si",
                "is_correct": False,
            },
            {
                "answer_text": "No",
                "is_correct": True,
            },
        ],
    },
    {
        "question_text": "Bañar a un animal de compañía en fuentes ornamentales, ¿Se considera una infracción?",
        "answers": [
            {
                "answer_text": "Si",
                "is_correct": True,
            },
            {
                "answer_text": "No",
                "is_correct": False,
            },
        ],
    },
    {
        "question_text": "Si una persona reincide cometiendo infracciones leves, ¿Pasa a ser una infracción grave?",
        "answers": [
            {
                "answer_text": "Si",
                "is_correct": True,
            },
            {
                "answer_text": "No",
                "is_correct": False,
            },
        ],
    },
    {
        "question_text": "Si una persona reincide cometiendo infracciones leves, ¿Pasa a ser una infracción muy grave?",
        "answers": [
            {
                "answer_text": "Si",
                "is_correct": False,
            },
            {
                "answer_text": "No",
                "is_correct": True,
            },
        ],
    },
    {
        "question_text": "Si una persona reincide cometiendo infracciones leves, ¿Sigue siendo leve?",
        "answers": [
            {
                "answer_text": "Si",
                "is_correct": False,
            },
            {
                "answer_text": "No",
                "is_correct": True,
            },
        ],
    },
    {
        "question_text": "¿Cuántas horas de servicio comunitario se debe cumplir por una infracción leve?",
        "answers": [
            {
                "answer_text": "Ninguna, solo pagar la multa.",
                "is_correct": False,
            },
            {
                "answer_text": "10 horas.",
                "is_correct": False,
            },
            {
                "answer_text": "24 horas.",
                "is_correct": False,
            },
            {
                "answer_text": "48 horas.",
                "is_correct": True,
            },
        ],
    },
    {
        "question_text": "Si un animal de compañía no cuenta con su calendario de vacunación y desparasitación, su responsable está cometiendo una infracción:",
        "answers": [
            {
                "answer_text": "Leve",
                "is_correct": True,
            },
            {
                "answer_text": "Grave",
                "is_correct": False,
            },
            {
                "answer_text": "Muy grave",
                "is_correct": False,
            },
        ],
    },
    {
        "question_text": "Si un animal de compañía está deambulando por espacio público sin collar, su responsable está cometiendo una infracción:",
        "answers": [
            {
                "answer_text": "Leve",
                "is_correct": True,
            },
            {
                "answer_text": "Grave",
                "is_correct": False,
            },
            {
                "answer_text": "Muy grave",
                "is_correct": False,
            },
        ],
    },
    {
        "question_text": "Si una persona no recoge los desechos fisiológicos de su animal de compañía, puede pagar una multa del ____ del salario básico unificado:",
        "answers": [
            {
                "answer_text": "10%",
                "is_correct": False,
            },
            {
                "answer_text": "20%",
                "is_correct": False,
            },
            {
                "answer_text": "30%",
                "is_correct": True,
            },
            {
                "answer_text": "40%",
                "is_correct": False,
            },
        ],
    },
    {
        "question_text": "Incumplir el uso de zonas caninas públicas es considerada una infracción:",
        "answers": [
            {
                "answer_text": "Leve",
                "is_correct": True,
            },
            {
                "answer_text": "Grave",
                "is_correct": False,
            },
            {
                "answer_text": "Muy grave",
                "is_correct": False,
            },
        ],
    },
    {
        "question_text": "¿Prohibir la interacción de un animal de compañía con otros de su especie es una infracción?",
        "answers": [
            {
                "answer_text": "Si",
                "is_correct": True,
            },
            {
                "answer_text": "No",
                "is_correct": False,
            },
        ],
    },
    {
        "question_text": "Las infracciones leves se deben pagar con el 30% del salario básico y con 60 horas de servicio comunitario?",
        "answers": [
            {
                "answer_text": "Si",
                "is_correct": False,
            },
            {
                "answer_text": "No",
                "is_correct": True,
            },
        ],
    },
    {
        "question_text": "Las infracciones leves se deben pagar con el 30% del salario básico y con 48 horas de servicio comunitario?",
        "answers": [
            {
                "answer_text": "Si",
                "is_correct": True,
            },
            {
                "answer_text": "No",
                "is_correct": False,
            },
        ],
    },
]

questions_collection.insert_many(questions_data)


# Close the MongoDB connection
client.close()
