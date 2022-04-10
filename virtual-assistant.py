import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia

name = 'Alexa'

listener = sr.Recognizer()
engine = pyttsx3.init()

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()
 


def listen():
    speech = ''
    try:

        with sr.Microphone() as source:
            print("Listening...")
            voice = listener.listen(source)
            rec = listener.recognize_google(voice, language='es-ES')
            rec = rec.lower()
            if name in rec:
                rec = rec.replace(name, '')
                print(rec)
                speech = rec
    except:
        pass
    return speech

def run():
    rec = listen()
    if rec != '':
        if 'reproduce' in rec:
            music = rec.replace('reproduce', '')
            talk('reproduciendo '+music)
            pywhatkit.playonyt(music)
        
        elif 'hora' in rec:
            hora = datetime.datetime().now()
            talk("Son las "+hora)
        elif 'busca' in rec:
            order = rec.replace('busca', '')
            info = wikipedia.summary(order, 1)
            talk(info)
        else:
            talk('Lo siento, no entendí, podrías repetirlo...')
    else:
        talk('si me estás hablando a mi, di mi nombre...')

#uncomment this lines to avoid the program finish

#while (True):
run() 

