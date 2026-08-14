import firebase_admin
from firebase_admin import credentials, firestore

from config.keyconfig import FIREBASE_KEYCONFIG_PATH


firestore_credentials = credentials.Certificate(cert=FIREBASE_KEYCONFIG_PATH)

_db = None

def get_db():
    global _db
    if _db is None:
        firebase_admin.initialize_app(firestore_credentials)
        _db = firestore.client()

    return _db
