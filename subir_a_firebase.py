import firebase_admin
from firebase_admin import credentials, firestore
from datetime import datetime

cred = credentials.Certificate("credenciales.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

def subir_datos(artista, cancion, emisora):
    data = {
        "artista": artista,
        "cancion": cancion,
        "emisora": emisora,
        "fecha": datetime.now().isoformat()
    }
    db.collection("monitoreo").add(data)