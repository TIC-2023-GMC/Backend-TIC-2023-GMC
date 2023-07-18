import firebase_admin
from firebase_admin import credentials

# import os


def initialize_firebase():
    # account_key_path = os.getenv("FIREBASE_ACCOUNT_KEY_PATH")
    # Load Firebase credentials from the JSON file
    cred = credentials.Certificate(
        "C:/Users/usuario/Desktop/Firebase_Key/pawq-fc6dc-firebase-adminsdk-3tf6e-aec938493d.json"
    )

    # Initialize the Firebase Admin SDK
    app = firebase_admin.initialize_app(
        cred, options={"storageBucket": "pawq-fc6dc.appspot.com"}
    )
    return app
