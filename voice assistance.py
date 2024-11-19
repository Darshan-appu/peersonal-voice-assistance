import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime
import pyjokes
import os
import time

def sptext():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Speak anything...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        try:
            print("Recognizing...")
            data = recognizer.recognize_google(audio)
            print(data)
            return data
        except sr.UnknownValueError:
            print("Could not understand")
            return ""

def speechtx(x):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    rate = engine.getProperty('rate')
    engine.setProperty('rate', 150)
    engine.say(x)
    engine.runAndWait()

if __name__ == '__main__':
    if "hello robo" in sptext().lower():
        speechtx("yes darshan tell me what you want to speak with me......")
        while True:
            data1 = sptext().lower()
            if "your name" in data1:
                name = "Myself nagamani"
                speechtx(name)

            elif "your age" in data1:
                age = "I was build today hence i am 2hours old"
                speechtx(age)
                
            elif "who created you" in data1:
                age = "darshan build me today"
                speechtx(age)
                
            elif "kothi" in data1:
                name = "yoshik is kothi"
                speechtx(name)

            elif 'time' in data1:
                current_time = datetime.datetime.now().strftime("%I:%M %p")
                speechtx(current_time)

            elif 'youtube' in data1:
                speechtx("OK Darshan, I will open it")
                webbrowser.open("https://www.youtube.com/")
                speechtx("Here it is")

            elif "joke" in data1:
                joke_1 = pyjokes.get_joke(language="en", category="all")
                print(joke_1)
                speechtx(joke_1)

            elif "play video" in data1:
                address = r"C:\Users\manas\OneDrive\Desktop\clips\videos"
                listvideos = os.listdir(address)
                print(listvideos)
                speechtx("OK Darshan, I am playing your video")
                os.startfile(os.path.join(address, listvideos[0]))

            elif "exit" in data1:
                speechtx("I am signing off Darshan. Whenever you need any help from me, feel free to ask.")
                break

            time.sleep(5)
    else:
        print("Thanks")
