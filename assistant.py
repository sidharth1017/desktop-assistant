import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition 
import datetime
import wikipedia #pip install wikipedia
import webbrowser #pip install webbrowser
import os
import smtplib
import random

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishme():                  
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")            
         
    elif hour>=12 and hour<18 :
        speak("Good Afternoon!")
    
    else:
        speak("Good Evening!")
    
    speak("I am siddharth's assistant. please tell me how may i help you")

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        audio = r.listen(source)
         
    try:
        print("Recognising.....")
        query = r.recognize_google(audio, language='en=in')
        print(f"user said: {query}\n")

    except Exception as e:
        print(e)

        print("say that again please ....")
        return"None"
    return query

# def sendEmail(to,content):
#     server = smtplib.SMTP('smpt.gmail.com', 587)
#     server.ehlo()
#     server.starttls()
#     server.login("youremail@gmail.com", 'your-password')
#     server.sendmail('youremail@gmail.com', to ,content)
#     server.close()



if __name__ == "__main__":
    wishme()
    takecommand()
    # while True:
    # #if 1:
    #     query = takecommand().lower()
    #     print(query)
    #     if 'wikipedia' in query:
    #         speak('Searching Wikipedia....')
    #         query = query.replace('wikipedia', "")
    #         results = wikipedia.summary(query, sentences=2 )                                                                                                                                                                                                                                                                                
    #         speak('Acoording to Wikipeadia')
    #         print(results)
    #         speak(results)

    #     elif "open youtube" in query:
    #         webbrowser.open("youtube.com")
    #         speak("opening youtube")
                
    #     if "play songs on youtube" in query:
    #             webbrowser.open('music.youtube.com')

              
       
    #     elif "open google" in query:
    #         webbrowser.open("google.com")
    #         speak("opening google")

    #     elif "play music " in query:
    #         music_dir = 'D:\\music\\songs'
    #         songs = os.listdir(music_dir)
    #         print(songs)
    #         os.startfile(os.path.join(music_dir,songs[0]))
            
    #     elif 'the time' in query:
    #         strTime = datetime.datetime.now().strftime("%H:%M:%S")
    #         speak(f"sir, the time is (strTime)")

    #     elif 'open code' in query:
    #         codepath = "E:\\Microsoft VS Code\\Code.exe"
    #         os.startfile(codepath)
    #         speak("opening vs code")

    #     elif 'open command' in query:
    #         commandpath = "cmd.exe"
    #         os.startfile(commandpath)
    #         speak("opening command")

    #     elif 'email to sidharth' in query:
    #         try:
    #             speak("what should i say?")
    #             content = takecommand()
    #             to = "sidharth@gmail.com"
    #             sendEmail(to, content)
    #             speak("Email has been sent!!")
    #         except Exception as e:
    #             print(e)
    #             speak("sorry my friend. I am not able to send this email")

    #     elif 'open github' in query:
    #         githubpath = "C:\\Users\\sidharth\\AppData\\Local\\GitHubDesktop\\GitHubDesktop.exe"
    #         os.startfile(githubpath)

    #     elif 'Who is siddharth' in query:
    #         print("Siddharth is who made me by python progamme")
    #         speak(results)

    #     elif 'quit' in query:
    #         exit()
    #         speak("closing jarvis")
    
        
            
        
        

                                                      

        
            

