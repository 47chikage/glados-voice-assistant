from utils.tools import prepare_text
from scipy.io.wavfile import write
import time
from sys import modules as mod
from utils.mind_tools import *
try:
    import winsound
except ImportError:
    from subprocess import call

def start_engine():
    print("Initializing TTS Engine...")
    device = 'cpu'
    glados = torch.jit.load('models/glados.pt')
    vocoder = torch.jit.load('models/vocoder-gpu.pt', map_location=device)

    for i in range(4):
        init = glados.generate_jit(prepare_text(str(i)))
        init_mel = init['mel_post'].to(device)
        init_vo = vocoder(init_mel)
    return device,vocoder,glados

device,vocoder,glados=start_engine()

def glados_speak(text):
    x = prepare_text(text).to('cpu')
    with torch.no_grad():
        old_time = time.time()
        tts_output = glados.generate_jit(x)

        old_time = time.time()
        mel = tts_output['mel_post'].to(device)
        audio = vocoder(mel)

        audio = audio.squeeze()
        audio = audio * 32768.0
        audio = audio.cpu().numpy().astype('int16')
        output_file = ('temp.wav')
        write(output_file, 22050, audio)

        if 'winsound' in mod:
            winsound.PlaySound(output_file, winsound.SND_FILENAME)
        else:
            call(["aplay", "./temp.wav"])

def glados_think(text):
    sentence = text
    sentence = tokenize(sentence)
    X = bag_of_words(sentence, all_words)
    X = X.reshape(1, X.shape[0])
    X = torch.from_numpy(X).to(device)

    output = model(X)
    _, predicted = torch.max(output, dim=1)

    tag = tags[predicted.item()]

    probs = torch.softmax(output, dim=1)
    prob = probs[0][predicted.item()]
    if prob.item() > 0.75:
        for intent in intents['intents']:
            if tag == intent["tag"]:
                return random.choice(intent['responses'])
    else:
        return ""