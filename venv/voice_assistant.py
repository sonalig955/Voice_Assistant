import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import sys
import wolframalpha
import os


engine = pyttsx3.init('sapi5')
client = wolframalpha.Client("AVKQ9P-XVTAAQKR49")
voices = engine.getProperty('voices')

engine.setProperty('voice' , voices[0].id)

def assistant_speaks(output):
    global num

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good morning!")
    elif hour>=12 and hour<16:
        speak("Good afternoon!")
    else:
        speak("Good evening!")

    speak("Hello ma'am, I am your personal assistant John")
    speak('How may I help you')

def takeCommand():
    #its take a microphone inputs from the user and return string output
    r=sr.Recognizer()
    with sr.Microphone()as source:
        print("Listening.....")
        r.pause_threshold = 0.8
        audio= r.listen(source)

    try:
        print("Recognizing...")
        query=r.recognize_google(audio,language="en-in")
        print(f"User said:{query}\n ")

    except Exception as e:
        print(e)
        speak("Say it again please i won't hear that....")
        return "None"
    return query

if __name__ =="__main__":
    wishMe()
    while True:
    #if 1:
        query = takeCommand().lower()

        #logic for execution task based on query

        if 'wikipedia' in query:
            speak("Searching Wikipedia...")
            query=query.replace("Wikipedia", " ")
            results = wikipedia.summary(query,sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
            speak("next command ma'am please")

        elif 'open youtube' in query:
            speak("Opening Youtube please Wait....")
            webbrowser.open("youtube.com")
            speak("next command ma'am please")

        elif 'who are you john' in query:
            speak("I am your personal assistant john")
            assistant_speaks(speak)
            speak("next command ma'am please")

        elif 'where are you john' in query:
            speak("I live right here in your device ma'am and i am available 24 into 7 to help you")
            assistant_speaks(speak)
            speak("next command ma'am please")
            
               
        elif 'what do you want' in query:
            speak("i want some love")
            assistant_speaks(speak)
            speak("next command ma'am please")
            

        elif 'i love you' in query:
            speak("love makes the world go round, i am so happy to be by your side")
            assistant_speaks(speak)
            speak("next command ma'am please")


        elif 'how are you' in query:
            speak("Good! Hope you're doing well too.how may i help?")    
            assistant_speaks(speak)
            speak("next command ma'am please")

        elif 'open google' in query:
            speak("Opening google please Wait....")
            webbrowser.open("google.com")
            speak("next command ma'am please")


        elif 'open stackoverflow' in query:
            speak("Opening stackoverflow please wait.....")
            webbrowser.open("stackoverflow.com")
            speak("next command ma'am please")

        elif 'the time' in query:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            print(strTime)
            speak(f"ma'am, the time is {strTime}") 
            speak("next command ma'am please")


        elif "quit" in query:
             speak("okay ma'am")
             speak("Bye ma'am, have a good day.")
             sys.exit()

    


        else:
            query = query
            speak("I can search the web for you,waiting")
            try:
                try:
                    res = client.query(query)
                    results = next(res.results).text
                    speak('WOLFRAM-ALPHA says - ')
                    speak('Got it.')
                    speak(results)

                except:
                    results = wikipedia.summary(query, sentences=2)
                    speak('Got it.')
                    speak('WIKIPEDIA says - ')
                    speak(results)

            except:
                webbrowser.open('www.google.com')
     
                
        

