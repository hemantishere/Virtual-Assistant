import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
from email_bot import email_automate

listener = sr.Recognizer()
engine = pyttsx3.init()

def listen_user():
    try:
        with sr.Microphone() as source:
            print("listening")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'assistant' in command:
                command = command.replace("assistant","")
            return command

    except:
        pass


def talk(text):
    engine.say(text)
    engine.runAndWait()

def assistant():
    talk("Hi there Hemant,Welcome to your own virtual assistant.. How May i help you today?")
    command = listen_user()

    if command == None:
        talk("please say something")

    elif "play" in command:
        command = command.replace("play","")
        talk("Playing" + command)
        pywhatkit.playonyt(command)

    elif "time" in command:
        time = datetime.datetime.now().strftime("%I:%M %p" )
        talk("Current time is" + time)

    elif "Who is" in command:
        person = command.replace("who is","")
        info = wikipedia.summary(person,1)
        talk(info)

    elif "joke" in command:
        talk(pyjokes.get_joke())

    elif "send" and "email" in command:
        email_automate.get_email_info()

    else:
        talk("Please say from one of the commands")

while True:
    assistant()
