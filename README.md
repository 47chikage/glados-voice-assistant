# glados-voice-assistant
This is a (work in progress) glados voice assistant from portal games

##structure
i assembled multiple components to make this work
(links will be added later)
-glados voice model from glados-tts repository
-vosk api for the speech to text from vosk api repository 
-nlp model i made myself for the "thinking" part

## how it works
-text to speech is activated and listening
-when glados_think() returns a text means it understood and had a response using the nlp model
-response is passed as text to glados_speak() which says the sentence in the voice of glados

##future work
the nlp was made to detect commands if they start by execute (for now)
i am thinking of hardcoding this instead of relying on the unreliable ai

this work is done by assembling and refactoring code from 2 other brilliant repositories with addition from myself to tie everything together 
