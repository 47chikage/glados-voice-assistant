from glados import glados_speak,glados_think
import queue
import sounddevice as sd
from vosk import Model, KaldiRecognizer
import json
from pynput.keyboard import Key, Controller
import subprocess
from os import system
keyboard = Controller()
q = queue.Queue()
def callback(indata, frames, time, status):
    q.put(bytes(indata))

voice_model = Model(lang="en-us")
with sd.RawInputStream(samplerate=44100, blocksize = 8000,
        dtype="int16", channels=1, callback=callback):

    rec = KaldiRecognizer(voice_model, 44100)
    glados_speak("booting up now")
    glados_speak("oh it's you")
    while True:
        data = q.get()
        if rec.AcceptWaveform(data):
            text = json.loads(rec.Result())['text']
            print(text)
            if text =='switch window':
                keyboard.press(Key.alt)
                keyboard.press(Key.tab)
                keyboard.release(Key.tab)
                keyboard.release(Key.alt)
            elif text=='open vs code':
                subprocess.run(['code'])
            elif text=='open browser':
                system("xdg-open 'www.google.com'")
            elif text.startswith('search'):
                search=text[6:]
                system(f"xdg-open 'http://www.google.com/search?q={search}'")
            elif text !='':
                response = glados_think(text)
                if response!='':
                    glados_speak(response)
                    q.queue.clear()