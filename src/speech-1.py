#!/usr/bin/env python3
# Requires PyAudio and PySpeech.
 
import speech_recognition as sr
from time import ctime
import time
import datetime
import pendulum
import pytz
import os
from gtts import gTTS
from datetime import date

def utcnow():
    return datetime.datetime.now(tz=pytz.utc)
created_date = utcnow().isoformat()
lastupdated_date = created_date

currentDT = pendulum.now().isoformat()
 
def speak(audioString):
    print(audioString)
    tts = gTTS(text=audioString, lang='en')
    tts.save("audio.mp3")
    os.system("mpg321 audio.mp3")
 
def recordAudio():
    # Record Audio
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source)
 
    # Speech recognition using Google Speech Recognition
    data = ""
    try:
        # Uses the default API key
        # To use another API key: `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
        data = r.recognize_google(audio)
        print("You said: " + data)
    except sr.UnknownValueError:
        print("I could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Speech Recognition service; {0}".format(e))
 
    return data
 
def jarvis(data):
    if "how are you" in data:
        speak("I am fine")
        
    if "Where are you living" in data:
        speak("I am living in San Francisco")
        
    if "What is your name" in data:
        speak("My name is Isabella")
 
    if "what time is it" in data:
        dateAndTime=currentDT
        speak("The day and time is")
        speak(str(dateAndTime))
 
    if "where is" in data:
        data = data.split(" ")
        location = data[2]
        speak("Hold on Volkmar, I will show you where " + location + " is.")
        os.system("chromium-browser https://www.google.nl/maps/place/" + location + "/&amp;")
 
# initialization
time.sleep(2)
speak("Hi Volkmar, what can I do for you today?")
speak("I am here to answer your questions")
dateAndTime=currentDT
speak(dateAndTime)
while 1:
    data = recordAudio()
    jarvis(data)
