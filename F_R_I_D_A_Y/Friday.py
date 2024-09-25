import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import webbrowser
import os
import smtplib
import cv2

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("I am Friday. How may I help you?")       

def takeCommand():
    #It takes microphone input from the user and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        # print(e)    
        speak("Say that again please...")  
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your-password')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()
        # Logic for executing tasks based on query
        if 'YouTube' in query:
            webbrowser.open("youtube.com")
        elif 'music' in query:
            music_dir = 'C:/Users/HP/Music'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))
        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")
        elif 'open code' in query:
            codePath = "D:\\pythonprograms\\friday.py"
            os.startfile(codePath)
        elif 'open camera' in query:
            cap = cv2.VideoCapture(0)
            if not cap.isOpened():
                print("Error: Could not open camera.")
                continue
            while True:
                ret, frame = cap.read()
                cv2.imshow('Camera', frame)
                q = takeCommand().lower()
                if 'close camera' in q:
                    break
                elif 'how do i look' in q:
                    speak("You are looking very attractive")
            cap.release()
            cv2.destroyAllWindows()
        elif 'open gmail' in query:
            webbrowser.open("mail.google.com")
        elif 'Google' in query:
            webbrowser.open("google.com")
        elif 'fuck' in query:
            speak("Watch your language you rascal!")
        elif 'how are you' in query:
            speak("I'm Fine. How are you? Hope you are enjoying your day!")
        elif 'nice' in query:
            speak("Okay, let me know if you need any help.")
        elif 'who are you' in query:
            speak("I'm Female Replacement Intelligence Digital Assistant for Youth.")
        
        elif 'exit' in query:
            speak("exiting now! Have a nice day! Bye!")
            exit()


        '''
        elif 'open' in query:
            webbrowser.open("google.com/search=?")

        elif 'email to friend' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "yourfriendEmail@gmail.com"   
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry. I am not able to send this email")
        '''
