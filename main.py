from glados import glados_speak,glados_think
import queue
import sounddevice as sd
from vosk import Model, KaldiRecognizer
import json
q = queue.Queue()
def callback(indata, frames, time, status):
    q.put(bytes(indata))

voice_model = Model(lang="en-us")
with sd.RawInputStream(samplerate=44100, blocksize = 8000,
        dtype="int16", channels=1, callback=callback):

    rec = KaldiRecognizer(voice_model, 44100)

    while True:
        data = q.get()
        if rec.AcceptWaveform(data):
            text = json.loads(rec.Result())['text']
            if text !='':
                response = glados_think(text)
                if response!='':
                    glados_speak(response)
                    q.queue.clear()