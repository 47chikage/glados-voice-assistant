# GlaDos-voice-assistant
This is a (work in progress) glados voice assistant from portal games

## Structure
i assembled multiple components to make this work
- webscraping [glados voice lines](https://theportalwiki.com/wiki/GLaDOS_voice_lines) for obtaining glados dialogue
- glados voice model from [R2D2FISH glados-tts](https://github.com/R2D2FISH/glados-tts)
- vosk api for the speech to text from [vosk-api](https://github.com/alphacep/vosk-api)
- nlp model i made myself for the "thinking" part, use the glados.ipynb and the dataset contained inside extra to make one yourself

## How it works
- inside the main loop
- text to speech is activated and listening
- if the text is a command, it is executed and the loop start again
- when glados_think() returns a text means it understood and had a response using the nlp model
- response is passed as text to glados_speak() which says the sentence in the voice of glados

## Requirements 
as i have been pip installing half of pypi since i tried a lot of things i have no memory of the used packages i'll have to rebuild from scratch and make the requirements.txt

## What can it do
- open browser
- switch opened window (useful when you have 1 monitor and do web dev)
- do a simple google search
- grret
- compliment
- tell jokes
- say goodbye
- insult
- can be easily extended to do much more

## Bonus
check out [nerdaxic](https://github.com/nerdaxic/glados-voice-assistant) for a home voice assisstant as mine is made with a different purpose.

a  [demo](https://youtu.be/vGyWzCfpP4Q) of my voice assistant
