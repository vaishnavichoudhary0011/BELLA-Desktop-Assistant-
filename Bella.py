import pyaudio
import operator
import speedtest
import pyttsx3
import requests
from requests import api
from requests.api import request
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib
from requests import get
import cv2
import pyjokes
import sys
import pyautogui
from plyer import notification
from bs4 import BeautifulSoup


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voice', voices[1].id)

#text to speech
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

#to wish
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  
     
    assname =("Bella") 
    speak("I am your Assistant")
    speak(assname)       


#to convert voice into text
def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)


         # Now we will be using the try and catch
        # method so that if sound is recognized 
        # it is good else we will have exception 
        # handling

    try:
        print("Recognizing...")    
         # for Listening the command in indian
            # english we can also use 'hi-In' 
            # for hindi recognizing
        query = r.recognize_google(audio, language='ei-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query

#function to send email
def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('vaishnavichoudhary06@gmail.com', 'Password')
    server.sendmail('vaishnavichoudhary06@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query




        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            #print(results)

            speak(results)



        elif 'open notepad' in query:
            npath ="C:\\Windows\\System32\\notepad.exe"
            os.startfile(npath)
            speak('opening notepad...')

        #to close notepad
        elif 'close notepad' in query:
            speak("okay ,closing notepad")
            os.system("taskkill /f /im notepad.exe")          


        elif 'ip address' in query:
            ip = get('https://api.ipify.org').text
            speak(f"your IP address is {ip}")
            print("your IP address = ",ip)


        elif 'play song on youtube ' in query:
            webbrowser.open("https://www.youtube.com/watch?v=nkmNsAyqi1I&list=RDnkmNsAyqi1I&start_radio=1")
            #kit.playonyt("see you again")
            speak('Searching youtube...')

        elif 'open google' in query:
            speak("what should i search on google")
            cm = takeCommand().lower()
            webbrowser.open(f"{cm}")

        elif 'open command prompt' in query:
            os.system("start cmd")    

        elif 'open stack overflow' in query or "stack overflow" in query:
            webbrowser.open("https://stackoverflow.com/") 

                

        elif 'play music' in query:
            music_dir = 'F:\music'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"the time is {strTime}")

        elif 'open code blocks' in query:
             npath  = "C:\\Users\\ASUS\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\CodeBlocks"
             os.startfile(npath)
             speak('opening code blocks...')


        #secure-smtplib module used
        elif 'email to vaishnavi' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "vaishnavichoudhary06@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend harry bhai. I am not able to send this email")

        elif 'can you do for me' in query:
            speak('I can do multiple tasks for you sir. tell me whatever you want to perform sir')

        elif 'old are you' in query:
            speak("I am a little baby sir")  

                    

        elif 'exit' in  query:
            speak("good bye sir have a good day") 
            exit()

        elif 'open camera' in query:
            cap = cv2.VideoCapture(0)
            while True:
                ret ,img =cap.read()
                cv2.imshow('webcam', img)
                k=cv2.waitKey(50)
                if k==27:
                    break;
            cap.release() 
            cv2.destroyAllWindows() 
            speak("opening camera")

    
        
        elif 'tell me a joke' in query:
           joke = pyjokes.get_joke()
           print(joke)
           speak(joke)  

        elif 'shut down the system ' in query:
            os.system("shutdown /s /t 5")  

        elif 'restart the system' in query:
            os.system("restart /r /t 5")    

        elif 'sleep the system' in query:
            os.system("rundll32.exe powrprof.dil,SetSuspendState 0,1,0")    

        elif "where is" in query:
            query = query.replace("where is", "")
            location = query
            speak("User asked to Locate")
            speak(location)
            webbrowser.open("https://www.google.nl/maps/place/"+ location + "")    

        
        elif 'set alarm' in query:
            speak("please tell me the time to set alarm. for example , set alaram to 5:30 a.m. ")
            tt = takeCommand()  #set alarm at 5:30 a.m.
            tt = tt.replace("set alarm to ","") #5:30 a.m.
            tt = tt.replace("." , "")#5:30 am
            tt = tt.upper() #5:30 AM
            import MyAlarm
            MyAlarm.alarm(tt)


       

        elif "temperature" in query:        
                search ="temperatur in nagpur"
                url = f"https://www.google.com/search?q={search}"
                r = requests.get(url)
                data = BeautifulSoup(r.text,"html.parser")
                temp = data.find("div",class_ = "BNeawe").text
                speak(f"current {search} is {temp}")



        elif "how much power left" in query:
            import psutil
            battery = psutil.sensors_battery()
            percentage = battery.percent
            speak(f"sir our system have {percentage} percent battery")
            if percentage>=75:
                speak("we have enough power to continue our work")
            elif  percentage>=40 and percentage<=75:
                speak("we should connect our system to charging point to charge our battery")
            elif percentage<=15 and percentage<=30:
                speak("we dont have enough power to work , please connect to charging")
            elif percentage<=15:
                speak("we have very low power , please connect to charging , the system will shutdown very soon")



        elif "take screenshot" in query:
            speak("sir , please tell me the name for this screenshot file")
            name = takeCommand().lower()
            speak("please sir hold the screen for few seconds , i am taking screenshot")
            img = pyautogui.screenshot()
            img.save(f"{name}.png")
            speak("i am done sir , the screenshot is saved in our main folder , now i am ready for next task")   



        elif "internet speed " in query:   
            speak("telling you your internet speed , wait for some seconds")
            st = speedtest.Speedtest()
            dl = st.download()
            up = st.upload()
            speak("sir we have {dl} bit per second downloading speed and {up} bit per second uploading speed")


        elif "you were born right" in query:
            speak(" hahah i was not born , i was developed ")  


        elif "good job" in query:
            speak("always here to help you")


        elif "open calculator" in query:
             npath ="C:\\Windows\\System32\\calc.exe"
             os.startfile(npath)
             speak("opening calculator for you")   


        elif 'close calculator' in query:
            speak("okay sir,closing calculator")
            os.system("taskkill /f /im calc.exe")      

        
        elif "what make you happy" in query or "what makes you happy" in query:
            speak("when you have fast internet speed, and i dont lag") 


        elif "how are you" in query:
            speak("i am fine , how are you")

        elif 'fine' in query or "good" in query:
            speak("It's good to know that your fine")   


        elif "who i am" in query:
            speak("If you talk then definitely your human.")     
            

        elif "change name" in query:
            speak("What would you like to call me ")
            assname = takeCommand()
            speak("Thanks for naming me")
 
        elif "what's your name" in query or "What is your name" in query:
            speak("My friends call me")
            speak(assname)
            print("My friends call me", assname)

        elif "Open instagram" in query:
            speak("opening instagram for you")
            webbrowser.open("https://www.instagram.com/")  
            
        elif "open facebook" in query:
            speak("Opening facebook ")
            webbrowser.open("https://www.facebook.com/")

        elif "show covid update" in query:
            speak("here is covid update ")
            webbrowser.open("https://www.worldometers.info/coronavirus/")      
           




        elif "today is " in query:
            day = datetime.datetime.today().weekday() + 1
      
    #this line tells us about the number 
    # that will help us in telling the day
            Day_dict = {1: 'Monday', 2: 'Tuesday', 
                3: 'Wednesday', 4: 'Thursday', 
                5: 'Friday', 6: 'Saturday',
                7: 'Sunday'}
      
            if day in Day_dict.keys():
                day_of_the_week = Day_dict[day]
                print(day_of_the_week)
                speak("The day is " + day_of_the_week)

        elif "you believe in god" in query:
            speak("i dont know which god human belive in , as you created me you are my god , thank you for developing me ")        

        elif "bye" in query:
            speak("Bye. have a nice day")
            exit()

        elif "thank you" in query:
            speak("welcome , happy to help you")
            exit()    

        elif "over bella" in query:
            speak("over and out")
            exit() 

        elif "bella" in query:
            speak("yes , i m here")
            print("yes i am here")

        elif "what is your name" in query:
            speak("my name is bella")    
            print("my name is bella")

        elif " i am bored" in query:
            speak("mmmmhhh , to be very frank , me too")
            print("mmmmhhh , to be very frank , me too")  

        elif "how was your day" in query:
            speak("i really had a very good day , what about you")    
            print("i really had a very good day , what about you")

        elif "not really great" in query:
            speak("it is okay , smile")

        elif "open google class room" in query or "open google classroom" in query:
            speak("opening google class room")
            webbrowser.open("https://classroom.google.com/u/0/h")



              

         
    

        

           
        