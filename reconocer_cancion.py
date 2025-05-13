import hashlib
import hmac
import base64
import time
import requests

def reconocer_cancion(nombre_archivo, acr_key, acr_secret, acr_host):
    with open(nombre_archivo, 'rb') as f:
        sample = f.read()

    http_method = "POST"
    http_uri = "/v1/identify"
    data_type = "audio"
    signature_version = "1"
    timestamp = str(int(time.time()))

    string_to_sign = f"{http_method}\n{http_uri}\n{acr_key}\n{data_type}\n{signature_version}\n{timestamp}"
    sign = base64.b64encode(
        hmac.new(acr_secret.encode('ascii'), string_to_sign.encode('ascii'), digestmod=hashlib.sha1).digest()
    ).decode('ascii')

    files = {
        'sample': sample,
        'access_key': acr_key,
        'data_type': data_type,
        'signature_version': signature_version,
        'signature': sign,
        'timestamp': timestamp,
    }

    url = f'https://{acr_host}/v1/identify'
    res = requests.post(url, files=files)
    return res.json()