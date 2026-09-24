import speech_recognition as sr
import pyttsx3
import sys
import pyaudiowpatch

sys.modules["pyaudio"] = pyaudiowpatch

engine = pyttsx3.init()

def speak(text):
    print("Assistant:", text)
    engine.say(text)
    engine.runAndWait()

recognizer = sr.Recognizer()

speak("Hello! I am your personal voice assistant. How can I help you?")

with sr.Microphone() as source:
    print("Listening...")
    audio = recognizer.listen(source)

try:
    command = recognizer.recognize_google(audio)
    print("You said:", command)
    speak("You said " + command)

except sr.UnknownValueError:
    speak("Sorry, I could not understand you.")

except sr.RequestError:
    speak("Sorry, there is a problem with the speech service.")