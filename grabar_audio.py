import os

def grabar_audio(nombre_archivo="sample.wav", stream_url="http://stream.radio.url/"):
    os.system(f"ffmpeg -y -i {stream_url} -t 15 -acodec pcm_s16le -ar 44100 -ac 1 {nombre_archivo}")