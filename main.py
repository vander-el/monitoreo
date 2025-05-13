from grabar_audio import grabar_audio
from reconocer_cancion import reconocer_cancion
from subir_a_firebase import subir_datos
import json

# Leer configuración
with open('config.json') as f:
    config = json.load(f)

EMISORA_URL = config['stream_url']
NOMBRE_ARCHIVO = config['audio_file']
EMISORA_NOMBRE = config['station_name']
ACR_KEY = config['acr_key']
ACR_SECRET = config['acr_secret']
ACR_HOST = config['acr_host']

# Ejecutar flujo completo
NOMBRE_ARCHIVO = "http://stream-uk1.radioparadise.com/mp3-128"
resultado = reconocer_cancion(NOMBRE_ARCHIVO, ACR_KEY, ACR_SECRET, ACR_HOST)

if resultado.get("status", {}).get("msg") == "Success":
    metadata = resultado["metadata"]["music"][0]
    titulo = metadata.get("title", "Desconocido")
    artista = metadata["artists"][0]["name"]
    print(f"Canción detectada: {titulo} - {artista}")
    subir_datos(artista, titulo, EMISORA_NOMBRE)
else:
    print("No se pudo reconocer la canción.")
