#!/usr/bin/python3

# import required modules
from gtts import gTTS 
from time import ctime
import webbrowser
import os 
import playsound 
import datetime 
import speech_recognition as sr 
import random 
import requests 
from bs4 import BeautifulSoup 
import pywhatkit 
import wikipedia 
import pyjokes 
from googletrans import Translator, constants 

class ALEXA:

    recognizer = sr.Recognizer()  # Initialize the recognizer

    def alexa_record(self):
        with sr.Microphone() as source:  # Use the Microphone class as a context manager to open and close the microphone
            print("Listening....")  # Print a message to indicate that the program is listening for audio input
            self.recognizer.adjust_for_ambient_noise(source, duration=1)
            audio = self.recognizer.listen(source)  # Capture the audio from the microphone and store it in the variable 'audio'
        return audio
        
    def alexa_speak(self, audios):
        tts = gTTS(text=audios, lang="en", slow=False)
        speech_file = "audio.mp3"
        tts.save(speech_file)
        playsound.playsound(speech_file)
        print(audios)
        os.remove(speech_file)

    def alexa_process(self, audio):
        try: 
            command=self.recognizer.recognize_google(audio, language="en") 
            print(f"you said {command}") 
            return command 
        
        except sr.UnknownValueError:
            # self.alexa_speak("sorry i did not get that")
            print("sorry i did not get that")
        except sr.RequestError:
            # self.alexa_speak("sorry Service is Down")
            print("sorry Service is Down")
        return ""


alexa = ALEXA()  # Initialize the ALEXA instance

def alexa_interface(exit) :
    global alexa
    audio = alexa.alexa_record()  # Record audio from the user
    command = alexa.alexa_process(audio)  # Recognize speech

    if "hello" in command or "Hi" in command or "Hey" in command  :
        alexa.alexa_speak("Hi Morgan How can i assist you")

    elif "Time" in command or "time" in command :
        time = ctime()
        alexa.alexa_speak("the time now is"+time)


    elif "Gpt" in command or "gpt"in command or "Chatgpt"in command or "chat gpt"in command or "Chat Gpt"in command or "Chat" in command or "chat"in command :
        url = "https://chatgpt.com"
        webbrowser.open(url)

    # elif "music" in command or "track" in command or "song"in command or "band" or "concert" in command :
    #     command = command.replace("alexa","")
    #     alexa.alexa_speak("here it is " + command) 
    #     pywhatkit.playonyt(command)

    elif "tell me about " in command :
        command = command.replace("alexa","")
        command = command.replace("tell me about","")
        info = wikipedia.summary(command,1)
        alexa.alexa_speak(info)

    elif "exit" in command :
        alexa.alexa_speak("Pleased to help you , Bye")
        exit = True
    return exit



def main():
    exit = False
    alexa.alexa_speak("Hi") 
    while True :  # Continuously listen for voice commands
        status =  alexa_interface(exit)
        if status :
            break
        

if __name__ == "__main__":
    main()
