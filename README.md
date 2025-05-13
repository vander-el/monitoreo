
# Monitoreo Radial Automático 🎧

Este proyecto permite grabar fragmentos de audio desde una emisora en línea, reconocer la canción usando ACRCloud y registrar los datos en Firebase Firestore.

## Archivos principales

- `main.py` – Ejecuta todo el proceso completo.
- `grabar_audio.py` – Captura 15 segundos de audio desde un stream.
- `reconocer_cancion.py` – Conecta con ACRCloud para detectar la canción.
- `subir_a_firebase.py` – Guarda el resultado en Firebase.
- `config.json` – Variables de configuración (usa variables de entorno).
- `requirements.txt` – Dependencias necesarias.

## Requisitos

- Python 3.9+
- Cuenta de ACRCloud (API Key, Secret y Host)
- Proyecto Firebase con Firestore y credenciales `credenciales.json`

## Uso

1. Instala las dependencias:

```bash
pip install -r requirements.txt
```

2. Exporta tus claves como variables de entorno:

```bash
export ACR_KEY=tu_clave
export ACR_SECRET=tu_secreto
export ACR_HOST=tu_host
```

3. Ejecuta el programa:

```bash
python main.py
```

## NOTA:
No incluyas `credenciales.json` en el repositorio público.
