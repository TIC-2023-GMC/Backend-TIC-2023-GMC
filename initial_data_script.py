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
            "img_path": "https://firebasestorage.googleapis.com/v0/b/pawq-fc6dc.appspot.com/o/Wordle-Icon.jpg?alt=media&token=c6ec60f7-abf4-424e-9660-be01598c46b5"
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
        "match_game_onboarding": "Adivina una palabra secreta. Tienes solo cinco intentos para adivinarla. Cada vez que haces una suposición, recibirás pistas: letras en su lugar correcto se mostrarán en verde y letras correctas en lugares incorrectos se mostrarán en amarillo. ¡Demuestra tus habilidades de deducción!",
    }
]
wordle_match_collection.insert_many(wordle_match_data)
# Words
wordle_words_collection = db["words_wordle"]
wordle_words_data = [
    {
        "wordle_game_clue": "Ley de Tenencia Responsable de Mascotas",
        "wordle_game_description": " Esta ley establece las responsabilidades de los propietarios de mascotas en Quito, incluyendo la obligación de proporcionarles cuidado adecuado, alimentación, atención veterinaria y evitar su abandono.",
        "wordle_game_words": ["Responsabilidad", "Obligacion", "Abandono"],
    },
    {
        "wordle_game_clue": "Registro de Mascotas",
        "wordle_game_description": "Los propietarios de mascotas en Quito deben registrar a sus animales en el sistema municipal, lo que les permite acceder a servicios de atención veterinaria y ayuda en caso de pérdida o robo.",
        "wordle_game_words": ["Registro", "Mascota", "Registrar"],
    },
    {
        "wordle_game_clue": "Vacunación y Esterilización",
        "wordle_game_description": "La ley exige que los perros y gatos en Quito sean vacunados y esterilizados, a menos que se obtenga un permiso especial para la cría de animales.",
        "wordle_game_words": ["Vacula", "Esterilizado", "Perro", "Gato"],
    },
    {
        "wordle_game_clue": "Prohibición de Razas Peligrosas",
        "wordle_game_description": "Algunas ciudades en Ecuador, incluyendo Quito, han implementado prohibiciones o restricciones en la tenencia de razas de perros consideradas peligrosas, como los pitbulls.",
        "wordle_game_words": ["Raza", "Quito", "Peligro"],
    },
    {
        "wordle_game_clue": "Sanciones por Incumplimiento",
        "wordle_game_description": "Los propietarios de mascotas que no cumplan con las leyes de tenencia responsable en Quito pueden enfrentar multas y sanciones, incluyendo la confiscación de sus animales.",
        "wordle_game_words": ["Sancion", "Multa", "Salario"],
    },
    {
        "wordle_game_clue": "Educación y Concientización",
        "wordle_game_description": "El gobierno de Quito ha implementado programas de educación y concientización sobre la tenencia responsable de mascotas, con el objetivo de promover el bienestar animal y reducir el abandono de animales.",
        "wordle_game_words": ["Educar", "Abandono", "Reducir"],
    },
    {
        "wordle_game_clue": "Responsabilidades Art. 3235: Control de Fauna Urbana",
        "wordle_game_description": "Identificación de animales con microchip ISO 11784/11785 o aprobado por la Secretaría de Salud Metropolitana. Debe ser realizado por veterinario acreditado y registrado en el Registro Metropolitano de Fauna Urbana (REMETFU).",
        "wordle_game_words": ["Microchip", "Veterinario", "Registro"],
    },
    {
        "wordle_game_clue": "Responsabilidades Art. 3235: Responsabilidad por Daños",
        "wordle_game_description": "Normativa sobre la responsabilidad por daños del animal, salvo circunstancias como provocación, defensa, actuación en propiedad privada y agresión en las primeras ocho semanas de maternidad, sujeto a criterio técnico del ente de Salud Metropolitano.",
        "wordle_game_words": ["Normativa", "Defensa", "Maternidad"],
    },
    {
        "wordle_game_clue": "Responsabilidades Art. 3235: Cuidado y Reconocimiento",
        "wordle_game_description": "Responsabilidad de cubrir gastos justificados por rescate, atención veterinaria, alimentación y cuidado al reconocer a organizaciones protectoras, individuos o al Centro de Atención Veterinaria, Rescate y Acogida Temporal (CAVRAT).",
        "wordle_game_words": ["Gastos", "Reconocimiento", "Cuidado"],
    },
    {
        "wordle_game_clue": "Responsabilidades Art. 3235: Transitar Seguro con Animales",
        "wordle_game_description": "Uso de collar, arnés, traílla u otros según el protocolo del ente rector de salud de Quito para seguridad propia y de terceros al transitar con animales.",
        "wordle_game_words": ["Collar", "Protocolo", "Seguridad"],
    },
    {
        "wordle_game_clue": "Responsabilidades Art. 3235: Higiene Responsable",
        "wordle_game_description": "Obligación de recoger los desechos de los animales bajo tu cuidado, tanto en lugares públicos como privados, como parte de una práctica de higiene responsable.",
        "wordle_game_words": ["Recoger", "Desechos", "Higiene"],
    },
    {
        "wordle_game_clue": "Responsabilidades Art. 3235: Hallazgo de Animales Extraviados",
        "wordle_game_description": "La persona que encuentre a un animal extraviado deberá reportar su hallazgo en la Unidad de Bienestar Animal, a través de los mecanismos que el Ente Rector Metropolitano de Salud desarrolle en el protocolo debidamente aprobado.",
        "wordle_game_words": ["Hallazgo", "Reportar", "Protocolo"],
    },
    {
        "wordle_game_clue": "Responsabilidades Art. 3235: Informe de Animales Extraviados",
        "wordle_game_description": "La persona que encuentre un animal extraviado debe informarlo a la Unidad de Bienestar Animal según el protocolo aprobado por el Ente Rector de Salud Metropolitano.",
        "wordle_game_words": ["Informe", "Animales", "Protocolo"],
    },
    {
        "wordle_game_clue": "Responsabilidades Art. 3235: Mantenimiento en Predios Privados",
        "wordle_game_description": "Mantener a los animales en predios privados, evitando su deambulación en el espacio público sin supervisión del responsable de su tenencia, de acuerdo con el Artículo 3235.",
        "wordle_game_words": ["Mantener", "Predios", "Supervisión"],
    },
    {
        "wordle_game_clue": "Responsabilidades Art. 3235: Tenencia en el Hogar",
        "wordle_game_description": "Respetar la tenencia responsable de animales en su lugar de habitación, ya sea propio o alquilado, en viviendas individuales o complejos habitacionales en propiedad horizontal, según el bienestar animal.",
        "wordle_game_words": ["Respetar", "Tenencia", "Hogar"],
    },
    {
        "wordle_game_clue": "Responsabilidades Art. 3235: Condiciones Inaceptables",
        "wordle_game_description": "Mantener animales, en habitáculos aislados o sin el espacio necesario para su tamaño y normal desenvolvimiento o expuestos a inclemencias del clima e insalubridad.",
        "wordle_game_words": ["Mantener", "Condiciones", "Aceptable"],
    },
    {
        "wordle_game_clue": "Prohibiciones Art. 3236: Maltrato Animal",
        "wordle_game_description": "Provocar en los animales daño o sufrimiento en cualquiera de sus formas.",
        "wordle_game_words": ["Maltrato", "Animales", "Daño"],
    },
    {
        "wordle_game_clue": "Prohibiciones Art. 3236: Abandono Animal",
        "wordle_game_description": "Abandonar animales en lugares públicos o privados, en áreas urbanas o rurales.",
        "wordle_game_words": ["Abandono", "Animales", "Lugares"],
    },
    {
        "wordle_game_clue": "Prohibiciones Art. 3236: Deambulación sin Supervisión",
        "wordle_game_description": "Permitir que los animales deambulen en el espacio público sin la debida supervisión.",
        "wordle_game_words": ["Deambulación", "Supervisión", "Animales"],
    },
    {
        "wordle_game_clue": "Prohibiciones Art. 3236: Espacios Anti-higiénicos",
        "wordle_game_description": "Mantener animales en espacios anti-higiénicos.",
        "wordle_game_words": ["Mantener", "Animales", "Higiénicos"],
    },
    {
        "wordle_game_clue": "Prohibiciones Art. 3236: Ataduras y Privación",
        "wordle_game_description": "Encadenar animales o atarlos como método habitual de mantenimiento en cautiverio, o privarlos de su movilidad natural.",
        "wordle_game_words": ["Ataduras", "Privación", "Animales"],
    },
    {
        "wordle_game_clue": "Prohibiciones Art. 3236: Mutilaciones Innecesarias",
        "wordle_game_description": "Evitar mutilaciones innecesarias o estéticas en animales, salvo por tratamiento veterinario necesario o esterilización.",
        "wordle_game_words": ["Evitar", "Mutilaciones", "Veterinario"],
    },
    {
        "wordle_game_clue": "Prohibiciones Art. 3236: Privación Alimentaria",
        "wordle_game_description": "Evitar privar a los animales de la alimentación esencial para su desarrollo o proporcionarles alimentos que puedan causarles daño o sufrimiento.",
        "wordle_game_words": ["Privar", "Alimentación", "Sufrimiento"],
    },
    {
        "wordle_game_clue": "Prohibiciones Art. 3236: Sustancias Venenosas",
        "wordle_game_description": "Administrar a los animales cualquier sustancia venenosa o tóxica, o provocar deliberadamente que el animal la ingiera.",
        "wordle_game_words": ["Administrar", "Sustancias", "toxica"],
    },
    {
        "wordle_game_clue": "Prohibiciones Art. 3236: Trabajo y Salud Animal",
        "wordle_game_description": "Obligar a animales a trabajar o producir mientras estén desnutridos, embarazadas, heridos o enfermos, evitando la sobreexplotación que amenace su salud física o psicológica, incluso si están saludables.",
        "wordle_game_words": ["Obligar", "Trabajo", "Salud"],
    },
    {
        "wordle_game_clue": "Prohibiciones Art. 3236: Peleas de Animales",
        "wordle_game_description": "Criar, reproducir, entrenar o utilizar animales para peleas, así como también, asistir, fomentar u organizar dichas peleas entre animales, entre animales y personas.",
        "wordle_game_words": ["Peleas", "Animales", "fomentar"],
    },
    {
        "wordle_game_clue": "Prohibiciones Art. 3236: Criaderos Responsables",
        "wordle_game_description": "Evitar reproducción anual en criaderos sin considerar características anatómicas, genéticas y psíquicas, que puedan afectar salud y bienestar de madre y crías. Abstenerse de practicar endogamia y criar razas braquicéfalas.",
        "wordle_game_words": ["Criaderos", "Reproducción", "Bienestar"],
    },
    {
        "wordle_game_clue": "Prohibiciones Art. 3236: Donación Inapropiada",
        "wordle_game_description": "Donar animales en calidad de premio, reclamo publicitario, recompensa, regalo de compensación.",
        "wordle_game_words": ["Regalo", "Animales", "Premio"],
    },
    {
        "wordle_game_clue": "Prohibiciones Art. 3236: Venta de Animales",
        "wordle_game_description": "Vender animales de compañía, excepto en los casos permitidos en la normativa metropolitana vigente.",
        "wordle_game_words": ["Vender", "Animales", "Compañía"],
    },
    {
        "wordle_game_clue": "Prohibiciones Art. 3236: Adopción Responsable",
        "wordle_game_description": "Dar en adopción o entregar animales de forma gratuita u onerosa a menores de edad o a personas que requieran tutoría.",
        "wordle_game_words": ["Edad", "Entregar", "Menor"],
    },
    {
        "wordle_game_clue": "Prohibiciones Art. 3236: Comercio Indigno",
        "wordle_game_description": "Utilizar animales de compañía para fines comerciales que atenten contra el bienestar animal.",
        "wordle_game_words": ["Comercio", "Animales", "Bienestar"],
    },
    {
        "wordle_game_clue": "Prohibiciones Art. 3236: Uso Dañino",
        "wordle_game_description": "Utilizar animales de compañía para dañar o causar muerte a otros animales.",
        "wordle_game_words": ["Utilizar", "Dañar", "Animales"],
    },
    {
        "wordle_game_clue": "Prohibiciones Art. 3236: Dejar en Vehículos",
        "wordle_game_description": "Dejar animales dentro de vehículos estacionados sin un tenedor responsable y bajo condiciones que atenten contra su bienestar o vida.",
        "wordle_game_words": ["Dejar", "Vehículos", "Bienestar"],
    },
    {
        "wordle_game_clue": "Prohibiciones Art. 3236: Adiestramiento Público",
        "wordle_game_description": "Adiestrar animales de compañía en el espacio público.",
        "wordle_game_words": ["Adiestrar", "Animales", "Público"],
    },
    {
        "wordle_game_clue": "Prohibiciones Art. 3236: Baño en Fuentes",
        "wordle_game_description": "Bañar animales de compañía en fuentes ornamentales.",
        "wordle_game_words": ["Bañar", "Animales", "Fuentes"],
    },
    {
        "wordle_game_clue": "Prohibiciones Art. 3236: Comercio Ambulatorio",
        "wordle_game_description": "Realizar comercio o ventas ambulatorias de animales vivos en el espacio público, tanto de forma habitual como ocasional.",
        "wordle_game_words": ["Comercio", "Ambulatorio", "Animales"],
    },
    {
        "wordle_game_clue": "Prohibiciones Art. 3236: Abuso Sexual Animal",
        "wordle_game_description": "Utilizar animales para zoofilia, pornografía o cualquier actividad sexual.",
        "wordle_game_words": ["Abuso", "Sexual", "Animales"],
    },
    {
        "wordle_game_clue": "Prohibiciones Art. 3236: Métodos de Caza",
        "wordle_game_description": "Usar métodos de caza o de control de depredadores naturales incluyendo los animales asilvestrados, que pudieran ocasionar daños a otros animales o a los seres humanos.",
        "wordle_game_words": ["Métodos", "Caza", "Daños"],
    },
    {
        "wordle_game_clue": "Prohibiciones Art. 3236: Métodos Perjudiciales",
        "wordle_game_description": "Evitar la comercialización o recomendación de métodos que causen daño físico o emocional a animales, como collares de ahogo, pinchos o descargas eléctricas, para su manejo, entrenamiento o adiestramiento.",
        "wordle_game_words": ["Evitar", "Métodos", "Daño"],
    },
    {
        "wordle_game_clue": "Prohibiciones Art. 3236: Animales Genéticamente Modificados",
        "wordle_game_description": "Crear o comercializar variedades nuevas de animales genéticamente modificados a través de selección artificial o ingeniería genética.",
        "wordle_game_words": ["Crear", "Genética", "Animales"],
    },
    {
        "wordle_game_clue": "Prohibiciones Art. 3236: Consumo de Animales de Compañía",
        "wordle_game_description": "Criar, comprar, mantener, capturar animales de compañía para consumo humano.",
        "wordle_game_words": ["Consumo", "Animales", "Compañía"],
    },
    {
        "wordle_game_clue": "Prohibiciones Art. 3236: Uso Criminal de Animales",
        "wordle_game_description": "Utilizar animales para el cometimiento de un delito o delitos.",
        "wordle_game_words": ["Utilizar", "Animales", "Delito"],
    },
    {
        "wordle_game_clue": "Prohibiciones Art. 3236: Obstrucción a Inspectores",
        "wordle_game_description": "Impedir la labor de los inspectores de la Dirección de Fauna Urbana o de la autoridad de control.",
        "wordle_game_words": ["Impedir", "Inspectores", "Obstrucción"],
    },
]
wordle_words_collection.insert_many(wordle_words_data)

# Game WordSearch
game_word_search_collection = db["game_word_search"]
game_word_search_data = [
    {
        "user_id": ObjectId("64c1b0ef0fd89c04b7114eb7"),
        "match_name": "Word Search Game Match",
        "match_game_onboarding": "N/A",
    }
]

game_word_search_collection.insert_one(game_word_search_data[0])

# Topics
topics_collection = db["topics_word_search"]
topics_data = [
    {
        "title": "Vacunación",
        "info": "Para asegurarte de que tu mascota esté sana y feliz, es necesario cuidarla adecuadamente. Una de las cosas esenciales que debes hacer es vacunarla. Las vacunas son muy importantes para tu amigo peludo, ya que evitan que se enferme gravemente o incluso muera por enfermedades. Las vacunas ayudan a fortalecer el sistema de defensa de tu mascota, manteniéndola protegida.",
        "statements": [
            {"clue": "Protege a tu mascota de enfermedades", "answer": "Vacuna"},
            {"clue": "Consecuencia de no vacunar a tu mascota", "answer": "Muerte"},
            {"clue": "Puede ocasionar la muerte de tu mascota", "answer": "Enfermedad"},
            {
                "clue": "Obligación y responsabilidad del dueño garantizarla",
                "answer": "Salud",
            },
            {
                "clue": "Beneficio que recibe una mascota tras la vacuna ante las enfermedades",
                "answer": "Inmunidad",
            },
        ],
    },
    {
        "title": "Desparasitación",
        "info": "No desparasitar a un animal de compañía puede ser perjudicial incluso para otras especies. Existen huevos de parásitos que están presentes en las heces de los animales de compañía y si estos son ingeridos por personas u otras especies pueden causar problemas graves como quistes en el hígado.",
        "statements": [
            {
                "clue": "Protege la salud de una mascota eliminado o impidiendo parásitos",
                "answer": "Desparasitar",
            },
            {
                "clue": "Cuando se ingieren sus huevos puede provocar quistes en hígado",
                "answer": "Parásitos",
            },
            {
                "clue": "Puede no presentar síntomas en una mascota",
                "answer": "Lombrices",
            },
            {
                "clue": "Están presentes en las heces de una mascota infectada",
                "answer": "Larvas",
            },
        ],
    },
    {
        "title": "Integración Comunitaria de Animales",
        "info": "Educar, socializar e integrar animales con la comunidad humana y animal, enfocándose en el bienestar, especialmente con perros y gatos.",
        "statements": [
            {"clue": "Considerado como animal de compañía", "answer": "Gatos"},
            {"clue": "Considerado como animal de compañía", "answer": "Perros"},
            {"clue": "Animal de compañía debe socializar con otros: ", "answer": "Animales"},
            {"clue": "Responsabilidad de un tutor", "answer": "Educar"},
        ],
    },
    {
        "title": "Riesgos de los Collares de Ahogo en Perros",
        "info": "Los collares de ahogo o castigo son perjudiciales para los perros.",
        "statements": [
            {"clue": "Evitan el Estrés", "answer": "Paseo"},
            {"clue": "Prohibido en Adiestramiento (Collar de)", "answer": "Ahogo"},
            {"clue": "Causa Ahogo", "answer": "Collar"},
            {"clue": "Collar de ", "answer": "Castigo"},
            {"clue": "Limitaciones Sociales", "answer": "perjudica"},
        ],
    },
    {
        "title": "Bienestar Animal y Cuidado Responsable",
        "info": "Tener un número de animales que puedan mantener de acuerdo al bienestar animal.",
        "statements": [
            {"clue": "Cuidado Responsable", "answer": "Animales"},
            {"clue": "Bienestar", "answer": "Mantener"},
            {"clue": "Número Adecuado", "answer": "Animales"},
        ],
    },
    {
        "title": "Alojamiento Adecuado para Animales",
        "info": "Proporcionar a los animales un alojamiento adecuado, manteniéndolos en buenas condiciones físicas, psíquicas y fisiológicas, de acuerdo a las necesidades de su especie.",
        "statements": [
            {"clue": "un buen ____ es necesario para un animal de compañía", "answer": "Alojamiento"},
            {"clue": "Necesidades Específicas y fisiológicas ___", "answer": "Fisicas"},
            {"clue": "Salud Mental", "answer": "Psíquicas"},
            {"clue": "Bienestar Fisiológico", "answer": "Animales"},
        ],
    },
    {
        "title": "Tratamientos Veterinarios para el Bienestar Animal",
        "info": "Someter a los animales, de manera oportuna, a los tratamientos veterinarios preventivos y curativos que pudieran precisar a fin de evitar daño, dolor o sufrimiento innecesario.",
        "statements": [
            {"clue": "Prevención", "answer": "Tratamientos"},
            {"clue": "Un animal de compañía debe recibir tramientos _____", "answer": "Veterinarios"},
            {"clue": "Cuidado prventivos y _____", "answer": "curativos"},
            {"clue": "Evitar Sufrimiento y _____", "answer": "Daño"},
        ],
    },
    {
        "title": "Socialización Segura de Animales",
        "info": "Socializar a los animales, bajo condiciones que no pongan en peligro la integridad física de las personas, otros animales o el propio animal, haciéndoles interactuar con la comunidad a fin de adaptarlos a una convivencia sana.",
        "statements": [
            {"clue": "Integración Comunitaria", "answer": "Socializar"},
            {"clue": "Se tiene que garantizar una convivencia ____", "answer": "Sana"},
            {"clue": "Interacción Segura", "answer": "Animales"},
            {"clue": "Integridad _____ se evita el peligro", "answer": "Fisica "},
        ],
    },

]

topics_collection.insert_many(topics_data)

# Close the MongoDB connection
client.close()
