#!pip install comtypes
 #!pip install pyttsx3
 #!pip install speechRecognition
# !pip install wikipedia
# !pip install webbrowser
# !pip install pipwin
# !pip install PyAudio
#Importing libraries
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import sys
#using api for giving laptop a voice 
engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voices',voices[1].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishme(datetime):
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("good morning")
    elif hour>12 and hour<18:
        speak("good afternoon")
    else:
        speak("good evening")
    speak("please let me know how can i help you")
def takecommand():
    # it take a microphone input from the user and returns string output
    r =sr.Recognizer()
    with sr.Microphone() as source:
         print("listening.....")
         r.pause_threshold  = 1
         audio=r.listen(source)
    try:
        print("recognizing.....")
        query = r.recognize_google(audio,language="en-in")
        print("user said:query")
    except Exception as e:
        print(e)
        speak("say that again please....")
        return "none"
    return query
if __name__=='__main__':
    #speak("Python is a high-level, general-purpose programming language.")
    wishme(datetime)
    #while true:
    if 1:
        query = takecommand().lower()
    
        if 'wikipedia'in query:
	        speak("Searching wikipedia......please wait for a while")
	        query=query.replace("wikipedia","")
	        results=wikipedia.summary(query,sentences=2)
	        speak=("According to wikipedia")
	        print(results)
            #speak(results)

        elif 'open youtube'in query:
            webbrowser.open("youtube.com")

        elif 'open google'in query:
            webbrowser.open("google.com")

        elif 'open notepad'in query:
            npath ='C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Accessories'
            os.startfile(npath)

        elif 'open command prompt'in query:
            os.system('stsrt cmd')

        elif'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        elif'open calender' in query:
            webbrowser.open("calender.com")

        elif'open code'in query:
            codepath ="C:\\users\\Rudra Trade\\appdata\\local\\programs\\microsoft vs code\\code.exe"
            os.startfile(codepath)
  
        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%h:%m:%S")
            speak(f"mam the time is{strTime}")

        elif 'no thanks' in query:
            speak("thank u sir for using me.have a good day")
        elif 'tell about sajan' in query:
            speak("hello world")
sys.exit()