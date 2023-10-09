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
user_favorite_publications = db["user_favorite_publications"]

users_data = [
    {
        "_id": ObjectId("64c1b0ef0fd89c04b7114eb7"),
        "first_name": "Gandhy",
        "last_name": "García",
        "mobile_phone": "0983473043",
        "neighborhood": "Cumbayá",
        "birth_date": datetime.datetime(1999, 11, 5),
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
        "photo": {
            "img_path": "https://scontent.fgye1-1.fna.fbcdn.net/v/t1.6435-9/74242360_3195954163812838_4274861617784553472_n.jpg?_nc_cat=110&ccb=1-7&_nc_sid=09cbfe&_nc_eui2=AeFRCjYsTZuQlf2PHyTPJ3HYymegSJbxrSjKZ6BIlvGtKPYIzlm5LEqBr9cR0tDl-FEvtHfkBqZQ6LHCgw-pkTlW&_nc_ohc=dye6H3TWD6QAX-v2xOF&_nc_ht=scontent.fgye1-1.fna&oh=00_AfCF85oDfvg1CEtIJ1We_mJ3gV49fRwyklxfDfl8SouHOA&oe=64D84DE2",
        },
    },
    {
        "_id": ObjectId("64c1b0ef0fd89c04b7114eb8"),
        "first_name": "Bill",
        "last_name": "Gates",
        "mobile_phone": "0988888881",
        "neighborhood": "Tumbaco",
        "birth_date": datetime.datetime(1955, 10, 28),
        "email": "bill.gates@outlook.es",
        "password": "password123",
        "num_previous_pets": 20,
        "num_current_pets": 10,
        "outdoor_hours": 12,
        "house_space": 3000,
        "has_yard": True,
        "main_pet_food": "homemade",
        "pet_expenses": 405,
        "motivation": "Love for animals",
        "photo": {
            "img_path": "https://imagenes.elpais.com/resizer/fdGn2HZ-QXQJW92FNbeWU7Z9Da4=/1960x1470/cloudfront-eu-central-1.images.arcpublishing.com/prisa/TW5CHJTUY5B3DOS35VMOLZUVF4.jpg",
        },
    },
    {
        "_id": ObjectId("64c1b0ef0fd89c04b7114eb9"),
        "first_name": "Barack",
        "last_name": "Obama",
        "mobile_phone": "0983473043",
        "neighborhood": "Cumbayá",
        "birth_date": datetime.datetime(1999, 11, 5),
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
        "photo": {
            "img_path": "https://upload.wikimedia.org/wikipedia/commons/8/8d/President_Barack_Obama.jpg",
        },
    },
    {
        "_id": ObjectId("64c1b0ef0fd89c04b7114eb0"),
        "first_name": "Donald",
        "last_name": "Trump",
        "mobile_phone": "0983473043",
        "neighborhood": "Cumbayá",
        "birth_date": datetime.datetime(1999, 11, 5),
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
        "photo": {
            "img_path": "https://fotografias.lasexta.com/clipping/cmsimages01/2023/08/02/790629EE-D19C-497E-8ECE-5BB0D4AE1307/imagen-archivo-donald-trump_98.jpg?crop=1920,1080,x0,y0&width=1900&height=1069&optimize=low&format=webply",
        },
    },
    {
        "_id": ObjectId("64c1b0ef0fd89c04b7114eb1"),
        "first_name": "Connor",
        "last_name": "Mason",
        "mobile_phone": "0913131313",
        "neighborhood": "San Antonio de Pichincha",
        "birth_date": datetime.datetime(1992, 12, 26),
        "email": "connor.mason@outlook.es",
        "password": "password123",
        "num_previous_pets": 23,
        "num_current_pets": 13,
        "outdoor_hours": 10,
        "house_space": 200,
        "has_yard": False,
        "main_pet_food": "homemade",
        "pet_expenses": 45,
        "motivation": "Love for animals",
        "photo": {
            "img_path": "https://everipedia-storage.s3-accelerate.amazonaws.com/ProfilePics/conor-mason__99848.png",
        },
    },
    {
        "_id": ObjectId("64c1b0ef0fd89c04b7114eb2"),
        "first_name": "Gustavo",
        "last_name": "Cerati",
        "mobile_phone": "0981234567",
        "neighborhood": "Solanda",
        "birth_date": datetime.datetime(1959, 8, 11),
        "email": "soygustavocerati@outlook.es",
        "password": "password123",
        "num_previous_pets": 2,
        "num_current_pets": 1,
        "outdoor_hours": 6,
        "house_space": 150,
        "has_yard": True,
        "main_pet_food": "Casera",
        "pet_expenses": 20.5,
        "motivation": "Amo a los animales",
        "photo": {
            "img_path": "https://akamai.sscdn.co/uploadfile/letras/fotos/3/a/7/5/3a75246b960d609112b5578f5774b3fe.jpg",
        },
    },
    {
        "_id": ObjectId("64c1b0ef0fd89c04b7114eb3"),
        "first_name": "Matt",
        "last_name": "Bellamy",
        "mobile_phone": "0983045817",
        "neighborhood": "Cumbayá",
        "birth_date": datetime.datetime(1978, 6, 9),
        "email": "museofficial@outlook.es",
        "password": "password123",
        "num_previous_pets": 5,
        "num_current_pets": 5,
        "outdoor_hours": 19,
        "house_space": 2050,
        "has_yard": True,
        "main_pet_food": "Sopas caseras",
        "pet_expenses": 40.5,
        "motivation": "Love for animals",
        "photo": {
            "img_path": "https://m.media-amazon.com/images/M/MV5BMTc4NzMzMTE3NV5BMl5BanBnXkFtZTcwMTQ0NTg2OA@@._V1_.jpg",
        },
    },
]
users_collection.insert_many(users_data)
user1 = users_collection.find_one({"first_name": "Gandhy"})
user2 = users_collection.find_one({"first_name": "Connor"})
user3 = users_collection.find_one({"first_name": "Gustavo"})
user4 = users_collection.find_one({"first_name": "Matt"})


# Adoption publications
adoption_publications_collection = db["adoption_publications"]
adoption_publications_data = [
    {
        "user": user1,
        "description": "Hermoso gato de 3 meses busca un hogar",
        "publication_date": datetime.datetime.now(datetime.timezone.utc)
        + datetime.timedelta(hours=-5),
        "photo": {
            "img_path": "https://scontent.fgye1-1.fna.fbcdn.net/v/t1.18169-9/536695_10200665558588650_1941658362_n.jpg?_nc_cat=106&ccb=1-7&_nc_sid=cdbe9c&_nc_eui2=AeH1q50jt5HgoS9npXdWLf1o3gXquT50xBLeBeq5PnTEEljZbDM758A0rOfiYECvjiE8vlhQ-yUUmKdFdDU59f_k&_nc_ohc=oR1QzT31QVUAX8xTWNQ&_nc_ht=scontent.fgye1-1.fna&oh=00_AfCapPgF09isXflAy1ql9TSyfw4rVU30HvueR9hG4xp3jA&oe=64D90FB8",
        },
        "likes": [],
        "species": "Gato",
        "pet_size": "Pequeño",
        "pet_breed": "Montés",
        "pet_age": 3,
        "pet_sex": True,  # boolean -> True: Male, False: Female
        "pet_location": "Cumbayá",
        "sterilized": True,
        "vaccination_card": False,
    },
    {
        "user": user2,
        "description": "Gatita de 1 año busca un hogar",
        "publication_date": datetime.datetime.now(datetime.timezone.utc)
        + datetime.timedelta(hours=-5),
        "photo": {
            "img_path": "https://www.tiendanimal.es/articulos/wp-content/uploads/2022/03/Gato-Singapura.jpg",
        },
        "likes": [],
        "species": "Gato",
        "pet_size": "Mediano",
        "pet_breed": "Singapura",
        "pet_age": 12,
        "pet_sex": False,  # boolean -> True: Male, False: Female
        "pet_location": "Solanda",
        "sterilized": False,
        "vaccination_card": False,
    },
    {
        "user": user3,
        "description": "Perrita de 3 años busca un hogar",
        "publication_date": datetime.datetime.now(datetime.timezone.utc)
        + datetime.timedelta(hours=-5),
        "photo": {
            "img_path": "https://fotografias.lasexta.com/clipping/cmsimages01/2022/08/09/3FFA8546-05CE-4608-9B69-6602D02A4C58/cachorro-pomsky_103.jpg?crop=1183,887,x0,y0&width=1200&height=900&optimize=low&format=webply",
        },
        "likes": [],
        "species": "Perro",
        "pet_size": "Mediano",
        "pet_breed": "Mestizo",
        "pet_age": 36,
        "pet_sex": False,  # boolean -> True: Male, False: Female
        "pet_location": "Tumbaco",
        "sterilized": True,
        "vaccination_card": True,
    },
]
adoption_publications_collection.insert_many(adoption_publications_data)

# Experience publications
experience_publications_collection = db["experience_publications"]
experience_publications_data = [
    {
        "user": user2,
        "description": "Mi gatita la conocí en la calle. Cuidarla es una de las mejores experiencias de mi vida. Recomiendo adoptar.",
        "publication_date": datetime.datetime.now(datetime.timezone.utc)
        + datetime.timedelta(hours=-5),
        "photo": {
            "img_path": "https://scontent.fgye1-1.fna.fbcdn.net/v/t1.18169-9/536695_10200665558588650_1941658362_n.jpg?_nc_cat=106&ccb=1-7&_nc_sid=cdbe9c&_nc_eui2=AeH1q50jt5HgoS9npXdWLf1o3gXquT50xBLeBeq5PnTEEljZbDM758A0rOfiYECvjiE8vlhQ-yUUmKdFdDU59f_k&_nc_ohc=oR1QzT31QVUAX8xTWNQ&_nc_ht=scontent.fgye1-1.fna&oh=00_AfCapPgF09isXflAy1ql9TSyfw4rVU30HvueR9hG4xp3jA&oe=64D90FB8",
        },
        "likes": [],
        "species": "Gato",
    },
    {
        "user": user4,
        "description": "Amo a mi perrita con todo mi corazón!",
        "publication_date": datetime.datetime.now(datetime.timezone.utc)
        + datetime.timedelta(hours=-5),
        "photo": {
            "img_path": "https://thumbs.dreamstime.com/b/perrita-chihuahua-acostado-sobre-fondo-gris-215147897.jpg",
        },
        "likes": [],
        "species": "Perro",
    },
]
experience_publications_collection.insert_many(experience_publications_data)

# Organizations
organizations_collection = db["organizations"]
organizations_data = [
    {
        "organization_name": "PAE: Protección Animal Ecuador",
        "organization_description": "La PAE es una organización sin fines de lucro que se dedica a promover el bienestar y la protección de los animales en Ecuador.",
        "organization_photo": {
            "img_path": "https://pae.ec/wp-content/uploads/2021/11/logotipo.png"
        },
        "external_links": {
            "facebook": "https://www.facebook.com/pae.ec/",
            "instagram": "https://www.instagram.com/paeecuador/",
            "twitter": "https://twitter.com/PAEecuador",
            "website": "https://pae.ec/",
        },
    },
    {
        "organization_name": "UBA: Unidad de Bienestar Animal",
        "organization_description": "La misión de UBA es gestionar la fauna urbana en Quito, priorizando el bienestar animal.",
        "organization_photo": {
            "img_path": "https://scontent.fuio35-1.fna.fbcdn.net/v/t39.30808-6/346650844_1321331818820153_5742948192253736333_n.jpg?_nc_cat=101&ccb=1-7&_nc_sid=a2f6c7&_nc_ohc=nJLpDiWJfXgAX9AKOQk&_nc_ht=scontent.fuio35-1.fna&oh=00_AfB_K0jsq2DbYFunGfeqydNX-jnqIg4DNYSwWt7dpfLgQw&oe=6523E82B"
        },
        "external_links": {
            "facebook": "https://www.facebook.com/UBAdeQuito",
            "instagram": "https://www.instagram.com/uba_quito/",
            "twitter": "https://twitter.com/UBA_Quito",
            "website": "",
        },
    },
    {
        "organization_name": "Fundación Segunda Oportunidad",
        "organization_description": "Segunda Oportunidad es un colectivo de cuidadanos voluntarios que se dedican al cuidado de gatos en Quito.",
        "organization_photo": {
            "img_path": "https://scontent.fuio35-1.fna.fbcdn.net/v/t39.30808-6/326548865_1216758802381822_4422846810562884066_n.png?_nc_cat=100&ccb=1-7&_nc_sid=a2f6c7&_nc_ohc=-lR0WdbmpA8AX-PGPer&_nc_ht=scontent.fuio35-1.fna&oh=00_AfCXQXzUqngQWjeRrX8WR769Ivs5jpPfrkuYJJ-qxJ5lkQ&oe=6524849F"
        },
        "external_links": {
            "facebook": "https://www.facebook.com/fundacionsegop",
            "instagram": "https://www.instagram.com/fundacionsegop/",
            "twitter": "",
            "website": "https://segundaoportunidad.ec/",
        },
    },
    {
        "organization_name": "Fundación Lucky Bienestar Animal",
        "organization_description": "Fundación que se encarga de preservar el bienestar de nuestros animales que en su mayoría son rescatados a los cuales damos acogida.",
        "organization_photo": {
            "img_path": "https://www.fundacionlucky.org/images/lucky.png"
        },
        "external_links": {
            "facebook": "https://www.facebook.com/luckybienestaranimal",
            "instagram": "https://www.instagram.com/luckybienestaranimal/",
            "twitter": "",
            "website": "https://www.fundacionlucky.org/lucky",
        },
    },
    {
        "organization_name": "ADVA: Asociación para la Defensa de la Vida Animal",
        "organization_description": "Organización enfocada en la rescate y rehabilitación de animales en crisis a través de hogares temporales y un santuario de vida.",
        "organization_photo": {
            "img_path": "https://firebasestorage.googleapis.com/v0/b/pawq-fc6dc.appspot.com/o/huellitas_de_amor.png?alt=media&token=3f3a3b1a-5b0a-4b9a-8b0a-9b0a0e2b0b0a"
        },
        "external_links": {
            "facebook": "https://www.facebook.com/ADVAdefensavidaanimal/",
            "instagram": "https://www.instagram.com/advadefensavidaanimal/",
            "twitter": "https://twitter.com/GuerrerosADVA",
            "website": "https://www.advaec.org/",
        },
    },
    {
        "organization_name": "RUNA: Ecuador",
        "organization_description": "Agrupación de rescate animal cuyo objetivo es dar voz a los angelitos callejeros y cambiar su vida",
        "organization_photo": {
            "img_path": "https://scontent.fuio35-1.fna.fbcdn.net/v/t39.30808-6/326328261_1202079764031779_771119207773087668_n.jpg?_nc_cat=106&ccb=1-7&_nc_sid=52f669&_nc_ohc=m_lwB6_DD-sAX9kAt6t&_nc_ht=scontent.fuio35-1.fna&oh=00_AfBOZQPw318JSwh2HWpkZxQtH60nKsqxim3Egk4vCmjdwg&oe=6523F279"
        },
        "external_links": {
            "facebook": "https://www.facebook.com/ECRUNA/",
            "instagram": "https://www.instagram.com/runa_ecuador/",
            "twitter": "",
            "website": "",
        },
    },
    {
        "organization_name": "Fundación Camino a Casa",
        "organization_description": "Fundación que tiene como objetivo rescatar perros y gatos en condiciones de vulnerabilidad, darles la mejor atención veterinaria, y encontrar su camino a casa.",
        "organization_photo": {
            "img_path": "https://fundacioncaminoacasa.com/wp-content/themes/yootheme/cache/49/logo_camino-492c4d4a.webp"
        },
        "external_links": {
            "facebook": "https://www.facebook.com/fundcaminoacasaecuador",
            "instagram": "https://www.instagram.com/caminoacasaec/",
            "twitter": "",
            "website": "https://fundacioncaminoacasa.com/",
        },
    },
]
organizations_collection.insert_many(organizations_data)

comments_collection = db["publication_comments"]

# Parishes
parishes_collection = db["parishes"]
parishes_data = [
    {"label": "Alangasí", "value": "Alangasí"},
    {"label": "Amaguaña", "value": "Amaguaña"},
    {"label": "Atahualpa", "value": "Atahualpa"},
    {"label": "Belisario Quevedo", "value": "Belisario Quevedo"},
    {"label": "Calacalí", "value": "Calacalí"},
    {"label": "Calderón", "value": "Calderón"},
    {"label": "Carcelén", "value": "Carcelén"},
    {"label": "Centro Histórico", "value": "Centro Histórico"},
    {"label": "Chavezpamba", "value": "Chavezpamba"},
    {"label": "Checa", "value": "Checa"},
    {"label": "Chilibulo", "value": "Chilibulo"},
    {"label": "Chillogallo", "value": "Chillogallo"},
    {"label": "Chimbacalle", "value": "Chimbacalle"},
    {"label": "Cochapamba", "value": "Cochapamba"},
    {"label": "Comité del Pueblo", "value": "Comité del Pueblo"},
    {"label": "Concepción", "value": "Concepción"},
    {"label": "Conocoto", "value": "Conocoto"},
    {"label": "Cotocollao", "value": "Cotocollao"},
    {"label": "Cumbayá", "value": "Cumbayá"},
    {"label": "El Condado", "value": "El Condado"},
    {"label": "El Inca", "value": "El Inca"},
    {"label": "El Quinche", "value": "El Quinche"},
    {"label": "Gualea", "value": "Gualea"},
    {"label": "Guamaní", "value": "Guamaní"},
    {"label": "Guangopolo", "value": "Guangopolo"},
    {"label": "Guayllabamba", "value": "Guayllabamba"},
    {"label": "Iñaquito", "value": "Iñaquito"},
    {"label": "Itchimbía", "value": "Itchimbía"},
    {"label": "Jipijapa", "value": "Jipijapa"},
    {"label": "Kennedy", "value": "Kennedy"},
    {"label": "La Argelia", "value": "La Argelia"},
    {"label": "La Ecuatoriana", "value": "La Ecuatoriana"},
    {"label": "La Ferroviaria", "value": "La Ferroviaria"},
    {"label": "La Libertad", "value": "La Libertad"},
    {"label": "La Mena", "value": "La Mena"},
    {"label": "La Merced", "value": "La Merced"},
    {"label": "Llano Chico", "value": "Llano Chico"},
    {"label": "Lloa", "value": "Lloa"},
    {"label": "Magdalena", "value": "Magdalena"},
    {"label": "Mariscal Sucre", "value": "Mariscal Sucre"},
    {"label": "Nanegal", "value": "Nanegal"},
    {"label": "Nanegalito", "value": "Nanegalito"},
    {"label": "Nayón", "value": "Nayón"},
    {"label": "Nono", "value": "Nono"},
    {"label": "Pacto", "value": "Pacto"},
    {"label": "Perucho", "value": "Perucho"},
    {"label": "Pifo", "value": "Pifo"},
    {"label": "Píntag", "value": "Píntag"},
    {"label": "Pomasqui", "value": "Pomasqui"},
    {"label": "Ponceano", "value": "Ponceano"},
    {"label": "Puéllaro", "value": "Puéllaro"},
    {"label": "Puembo", "value": "Puembo"},
    {"label": "Puengasí", "value": "Puengasí"},
    {"label": "Quitumbe", "value": "Quitumbe"},
    {"label": "Rumipamba", "value": "Rumipamba"},
    {"label": "San Antonio de Pichincha", "value": "San Antonio de Pichincha"},
    {"label": "San Bartolo", "value": "San Bartolo"},
    {"label": "San Juan", "value": "San Juan"},
    {"label": "San José de Minas", "value": "San José de Minas"},
    {"label": "Solanda", "value": "Solanda"},
    {"label": "Tababela", "value": "Tababela"},
    {"label": "Tumbaco", "value": "Tumbaco"},
    {"label": "Turubamba", "value": "Turubamba"},
    {"label": "Yaruquí", "value": "Yaruquí"},
    {"label": "Zámbiza", "value": "Zámbiza"},
]
parishes_collection.insert_many(parishes_data)

# Games
games_collection = db["games"]
games_data = [
    {
        "game_name": "Leyes y Sanciones",
        "game_description": "En este juego podrás aprender sobre las leyes y sanciones que existen en la ciudad de Quito para la protección de los animales.",
        "game_category": "Trivia",
        "game_image": {
            "img_path": "https://firebasestorage.googleapis.com/v0/b/pawq-fc6dc.appspot.com/o/hangman.png?alt=media&token=829fd1ad-f972-44cd-92e3-bf21b489da2b"
        },
    },
    {
        "game_name": "Cuidado Responsable",
        "game_category": "Puzzle",
        "game_description": "En este juego podrás aprender sobre el cuidado responsable de los animales de compañía.",
        "game_image": {
            "img_path": "https://firebasestorage.googleapis.com/v0/b/pawq-fc6dc.appspot.com/o/word_search.png?alt=media&token=5d324775-0f68-4bf6-92dc-bc85d69dbb5c"
        },
    },
    {
        "game_name": "Evaluándome",
        "game_description": "En este juego podrás responder preguntas sobre los animales de compañía.",
        "game_category": "Trivia",
        "game_image": {
            "img_path": "https://firebasestorage.googleapis.com/v0/b/pawq-fc6dc.appspot.com/o/quiz_game.png?alt=media&token=a586d2af-a788-4740-b56d-c69ee8adf16f"
        },
    },
]
games_collection.insert_many(games_data)

# Match
# Game Quiz
game_quiz_collection = db["game_quiz"]
game_quiz_data = [
    {
        "user_id": ObjectId("64c1b0ef0fd89c04b7114eb7"),
        "match_name": "Quiz Game Match",
        "match_game_score": 0,
        "match_game_time": 0,
        "match_game_onboarding": ".",
        "match_game_questions": [],
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

# Wordle Match
wordle_match_collection = db["wordle_match"]
wordle_match_data = [
    {
        "user_id": ObjectId("64c1b0ef0fd89c04b7114eb7"),
        "match_name": "Wordle Match",
        "match_game_score": 0,
        "match_game_time": 0,
        "match_game_onboarding": ".",
    }
]
wordle_match_collection.insert_many(wordle_match_data)
# Words
wordle_words_collection = db["words_wordle"]
wordle_words_data = [
    {
        "wordle_game_clue": "Pregunta 1",
        "wordle_game_description": "Descripción de la pregunta 1",
        "wordle_game_words": ["Palabra1", "Palabra2", "Palabra3"],
    },
    {
        "wordle_game_clue": "Pregunta 2",
        "wordle_game_description": "Descripción de la pregunta 2",
        "wordle_game_words": ["Palabra4", "Palabra5", "Palabra6"],
    },
    {
        "wordle_game_clue": "Pregunta 3",
        "wordle_game_description": "Descripción de la pregunta 3",
        "wordle_game_words": ["Palabra7", "Palabra8", "Palabra9"],
    },
    {
        "wordle_game_clue": "Pregunta 4",
        "wordle_game_description": "Descripción de la pregunta 4",
        "wordle_game_words": ["Palabra10", "Palabra11", "Palabra12"],
    },
    {
        "wordle_game_clue": "Pregunta 5",
        "wordle_game_description": "Descripción de la pregunta 5",
        "wordle_game_words": ["Palabra13", "Palabra14", "Palabra15"],
    },
    {
        "wordle_game_clue": "Pregunta 6",
        "wordle_game_description": "Descripción de la pregunta 6",
        "wordle_game_words": ["Palabra16", "Palabra17", "Palabra18"],
    },
    {
        "wordle_game_clue": "Pregunta 7",
        "wordle_game_description": "Descripción de la pregunta 7",
        "wordle_game_words": ["Palabra19", "Palabra20", "Palabra21"],
    },
    {
        "wordle_game_clue": "Pregunta 8",
        "wordle_game_description": "Descripción de la pregunta 8",
        "wordle_game_words": ["Palabra22", "Palabra23", "Palabra24"],
    },
    {
        "wordle_game_clue": "Pregunta 9",
        "wordle_game_description": "Descripción de la pregunta 9",
        "wordle_game_words": ["Palabra25", "Palabra26", "Palabra27"],
    },
    {
        "wordle_game_clue": "Pregunta 10",
        "wordle_game_description": "Descripción de la pregunta 10",
        "wordle_game_words": ["Palabra28", "Palabra29", "Palabra30"],
    },
]
wordle_words_collection.insert_many(wordle_words_data)

# Close the MongoDB connection
client.close()
