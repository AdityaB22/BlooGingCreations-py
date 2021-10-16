#Importing Libraries
import ntpath
from os import fsdecode, name
import os
from tkinter.constants import COMMAND
from googletrans import Translator
from tkinter.font import Font
from typing import Text
from requests import get
import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
from playsound import playsound
import wikipedia
import pyautogui
from tkinter import Label
from tkinter import Entry
from tkinter import Button
from tkinter import Tk
import dropbox
from tkinter import StringVar
from pytube import YouTube 
import smtplib
import speech_recognition as sr
import cv2
import screen_brightness_control as sbc
import pyjokes
import webbrowser
import subprocess
import requests, json , sys
#PyAudio
#PyWhatKit
#PyJokes
#Wikipedia
#OpenweatherApi

listener = sr.Recognizer()

engine = pyttsx3.init()
voices = engine.getProperty("voices")
engine.setProperty('voice', voices[0].id)

def engine_talk(text):
    engine.say(text)
    engine.runAndWait()
    
def weather(city):
    # Enter your API key here 
    api_key = "<YOUR API KEY"
    
    # base_url variable to store url 
    base_url = "http://api.openweathermap.org/data/2.5/weather?"

    # Give city name 
    city_name = city
    
    # complete_url variable to store 
    # complete url address 
    complete_url = base_url + "appid=" + api_key + "&q=" + city_name 
    
    # get method of requests module 
    # return response object 
    response = requests.get(complete_url) 
    
    # json method of response object  
    # convert json format data into 
    # python format data 
    x = response.json() 
    
    # Now x contains list of nested dictionaries 
    # Check the value of "cod" key is equal to 
    # "404", means city is found otherwise, 
    # city is not found 
    if x["cod"] != "404": 
    
        # store the value of "main" 
        # key in variable y 
        y = x["main"] 
    
        # store the value corresponding 
        # to the "temp" key of y 
        current_temperature = y["temp"] 
    
        # store the value corresponding 
        # to the "pressure" key of y 
        #current_pressure = y["pressure"] 
    
        # store the value corresponding 
        # to the "humidity" key of y 
        #current_humidiy = y["humidity"] 
    
        # store the value of "weather" 
        # key in variable z 
        #z = x["weather"] 
    
        # store the value corresponding  
        # to the "description" key at  
        # the 0th index of z 
        #weather_description = z[0]["description"]
        return str(current_temperature)
    
        # print following values 
        '''print(" Temperature (in kelvin unit) = " +
                        str(current_temperature) + 
            "\n atmospheric pressure (in hPa unit) = " +
                        str(current_pressure) +
            "\n humidity (in percentage) = " +
                        str(current_humidiy) +
            "\n description = " +
                        str(weather_description)) 
    else: 
        print(" City Not Found ")
        '''

def user_commands():
    try:
        with sr.Microphone() as source:
            print("listening...")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa', '')
                print(command)
    except:
        pass
    return command



def takecomand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 1
        audio = r.listen(source)



# wish me
def greetMe():
    currentH = int(datetime.datetime.now().hour)
    if currentH >= 0 and currentH < 12:
        engine_talk('Good Morning!')

    if currentH >= 12 and currentH < 18:
        engine_talk('Good Afternoon!')

    if currentH >= 18 and currentH !=0:
        engine_talk('Good Evening!')


greetMe()

engine_talk('Hello Sir, welcome I am your digital assistant !')
engine_talk('How may I help you?')

#to send email
def sendEmail(to, content):
    server = smtplib.SMTP('smpt.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('adiserhai@gmail.com, adityaabc123abc')
    server.sendmail('adiserhai@gmail.com',to, 'okfolderlogin99@gmail.com')
    server.close()
    
    
def run_alexa():
    command = user_commands()
    if 'play' in command:
        song = command.replace('play', '')
        #print('New Command is' +command)
        #print('The bot is telling us: Playing' +command)
        engine_talk('Playing' +song)
        pywhatkit.playonyt(song)


    def takeHindi():
        command = sr.Recognizer()
        with sr.Microphone() as source:
            print("listening....")
            command.pause_threshold = 1
            audio = command.listen(source)

            try:
                print("Recognizer...")
                command = command.recognize_google(audio, language = 'hi')
                print(f"you said : {command}")

            except Exception as Error:
                return "none"

            return command.lower()

    def tran():
        engine_talk("tell me the line, sir!")
        line = takeHindi()
        translate = Translator()
        result = translate.translate(line)
        Text = result.text
        engine_talk(f"the translator for this line is"+Text)






    if 'play' in command:
        song = command.replace('play', '')
        engine_talk('playing' + song)
        pywhatkit.playonyt('song')



    elif 'open youtube' in command:
        webbrowser.open('http://www.youtube.com/')
        engine_talk('opening youtube')


    elif 'open whatsapp web' in command:
        webbrowser.open('https://web.whatsapp.com')
        engine_talk('opening whatsapp web')


    elif 'open whatsapp' in command:
        webbrowser.open('http://web.whatsapp.com/')
        engine_talk('opening whatsapp')
    
    
    elif 'nothing' in command:
        engine_talk("ok sir,have a great day i want anything else then, i will try to do")
        sys.exit()
    
    
    elif 'open gmail' in command:
        webbrowser.open("http://gmail.com")
        engine_talk('opening gmail')
    
    
    elif 'open camera' in command:
        engine_talk('opening camera')
        cap = cv2.VideoCapture(0)
        while True:
            ret, img = cap.read()
            cv2.imshow('webcam', img)
            k = cv2.waitKey(50)
            if k==27:
                break;
        cap.releases()
        cv2.distroyAllWindows()


    elif 'voice' in command:
        engine_talk("go to 39 line of code and engine.setProperty'voice', voices[0].id in place of 0 write 1 for zeragirl voice")
    
    
    elif 'open touch typing' in command:
        webbrowser.open('https://www.typingstudy.com/lesson/2/extra_word_drill')
        engine_talk ('opening touch typing ,sir')



    elif 'volume up' in command:
        pyautogui.press('volumeup')
        engine_talk('volume up')
    
    
    elif 'volume down' in command:
        pyautogui.press('volumedown')
        engine_talk('volume down')
    
    
    elif 'volume mute' in command:
        pyautogui.press('volumemute')
        engine_talk('volume muting')
    
    
    elif 'increase volume' in command:
        pyautogui.press('volumeup')
        engine_talk('increasing volume')
    
    
    elif 'activate' in command:
        engine_talk('activating  sir')
    
    
    elif 'wake up' in command:
        engine_talk('waking up sir ')
    
    
    elif 'make a call ' in command:
        engine_talk('ok sir, t whome may i call')
    
    
    elif 'call to' in command:
        engine_talk('seen that the number is not there in your call log',)
    
    
    elif 'decrease volume' in command:
        pyautogui.press('volumedown')
        engine_talk('decreasing volume')
    
    
    elif 'mute' in command:
        pyautogui.press('volumemute')
        engine_talk('muting')
    
    
    elif 'unmute' in command:
        pyautogui.press('volumeunmute')
        engine_talk('unmuting')
    
    
    elif 'volume unmute' in command:
        pyautogui.press('volume unmute')
        engine_talk('volume unmuting')
    
    
    elif 'up volume' in command:
        pyautogui.press('volumeup')
        engine_talk('volume up')
    
    
    
    elif 'down volume' in command:
        pyautogui.press('volumedown')
        engine_talk('volume down')
    
    
    elif 'mute volume' in command:
        pyautogui.press('volume mute')
        engine_talk('volume muting')
    
    
    
    
    elif 'volume increase' in command:
        pyautogui.press('volumeup')
        engine_talk('volume increasing')
    
    
    elif 'down volume' in command:
        pyautogui.press('volume down')
        engine_talk('volume down')
    
    
    elif 'how are you' in command:
        engine_talk('fine, sir, how are you')
    
    elif 'fine' in command:
        engine_talk('ohk, its good to hear')
    

    elif 'translator' in command:
        tran()
    
    
    elif 'okay' in command:
        engine_talk('ok sir, me me another command')
    
    
    
    elif 'unmute volume' in command:
        pyautogui.press('volume unmute')
        engine_talk('volume unmuting')   
    
    
    
    elif 'what can you do' in command:
        engine_talk('you can say open social meadia apps or increase and decrease volume and many more!! ')
    
    
    elif 'you are great' in command:
        engine_talk('thanks for compliment but you are great too')
    
    
    elif 'i like talking with you' in command:
        engine_talk('i like talking to you too, i am glad i can hep you')
    
    
    elif 'remember that' in command:
        remeberMsg = command.replace("remember that","")
        engine_talk('you tell me to remember me that you need to make me advance by adding codes')
    
    
    elif 'wake up' in command:
        engine_talk('ok sir i am waking and your system will start in 2 seconds')
    
    
    elif 'search' in command:
            command = command
            engine_talk('Searching...')
            try:
                try:
                    res = command(command)
                    results = next(res.results).text
                    ('WOLFRAM-ALPHA says - ')
                    ('Got it.')
                    engine_talk(results)
                    
                except:
                    results = wikipedia.summary(command, sentences=2)
                    engine_talk('Got it.')
                    engine_talk('WIKIPEDIA says - ')
                    engine_talk(results)
        
            except:
                webbrowser.open('www.google.com')
        

    elif ' search' in command:
        query = command
        engine_talk('Searching...')
            
        try:
                    res = query(command)
                    results = next(res.results).text
                    engine_talk('WOLFRAM-ALPHA says - ')
                    engine_talk('Got it.')
                    engine_talk(results)
                    
        except:
                    results = wikipedia.summary(query, sentences=2)
                    engine_talk('Got it.')
                    engine_talk('WIKIPEDIA says - ')
                    engine_talk(results)
        
           






    elif 'motivational' in command:
        engine_talk('failures are the most important thing in life because  success dosent teach you as much it boosts you ego')
    
    
    elif 'open visual studio code' in command:
        codePath = "C:\\Users\\adise\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Visual Studio Code"
        engine_talk('opening visual studio code')
    
    
    elif 'open vs code' in command:
        codePath = "C:\\Users\\adise\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Visual Studio Code"
        engine_talk('opening vs code')
    
    
    elif 'open  code' in command:
        codePath = "C:\\Users\\adise\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Visual Studio Code"
        engine_talk('opening code')
    
    
    elif 'colse youtube' in command:
        os.system("taskkill /f /im youtube.com ")
        engine_talk('closing youtube')
    
    
    elif 'wait' in command:
        engine_talk('ok sir, waiting, whenever you want you can say to quit,stop or sleep, thanks you ')
    
    
    elif 'gravity movie' in command:
        moviePath ="C:\\"
        engine_talk('playing gravity movie')
    
    
    elif 'send an email'in command:
        try:
            engine_talk('what should i say or send in email message?')
            content = takecomand().lower()
            to = 'asaditya718@gmail.com'
            sendEmail(to, content)
            engine_talk('email has been sent')
        except Exception as e:
            print(e)
            engine_talk('sorry sir, i am not able to send the email')
    
    
    elif 'open facebook' in command:
        webbrowser.open('http://www.facebook.com/')
        engine_talk('opening facebook')
    
    
    
    elif 'what do you eat' in command:
        engine_talk('if i could, i would go from kanyakumari to kashimr tasting the different types of biryaanis.i really wand')
    
    
    
    elif 'what do you eat' in command:
        engine_talk('i love fetching on the knowledge')
    
    
    elif 'i will come after have my food' in command:
        engine_talk('ok sir , i would also go for having my food that is fetching knowledge')
    
    
    elif 'what is your favourite food' in command:
        engine_talk('i easily digest facts... and i like regurgitation them too, want to hear a fun fact, if want than speak yes i want to hear fun fact')
    
    
    elif 'yes i want to hear fact' in command:
        engine_talk('The world’s longest French fry is 34-inches long, if want to hear more than say tell me more facts')
    
    
    elif 'tell me more facts' in command:
        engine_talk('Garlic bulbs are full of Vitamin C, iron, potassium, magnesium, zinc and more. It also has 17 amino acids, from now if want to hear more facts say more facts ')
    
    
    elif 'tell me more facts' in command:
        engine_talk('On the South Atlantic island of Tristan da Cunha, potatoes were once used as currency.')
    
    
    elif 'facts' in command:
        engine_talk('Ice cream was once called “cream ice.')
    
    
    elif 'anydesk' in command:
        webbrowser.open('http://anydesk.com')
        engine_talk('opening anydesk')
    
    
    elif 'facts' in command:
            engine_talk('Apples float because they are one-quarter air!')
    
    
    elif 'open instagram' in command:
        webbrowser.open('http://www.instagram.com/')
        engine_talk('opening instagram')
    
    
    elif 'open twitter' in command:
        webbrowser.open('http://www.twitter.com/')
        engine_talk('opening twitter')
    
    
    elif 'open gmail' in command:
        webbrowser.open('http://www.gmail.com')
        engine_talk('opening gmail')
    
    
    elif 'open wikipedia' in command:
        webbrowser.open('http://www.wikipedia.com')
        engine_talk('opening wikipedia')
    
    
    elif 'open google chrome' in command:
        webbrowser.open_new_tab('http://www.google.co.uk/')
        engine_talk('opening google chrome')
    
    
    elif 'year' in command:
        year = datetime.datetime.now().strftime('%Y')
        engine_talk('Year is' +year )
    
    
    elif 'video downloader' in command:
        root = Tk()
        root.geometry('500x300')
        root.resizable(0, 0)
        root.title('youtube Video downloader')
        engine_talk('"enter Video URL here !')

        Label(root,Text = "youtube video downloader", font = 'arial 15 bolt').pack
        link = StringVar()
        Label(root, 'paste yt video URL here', 'arial 15 bolt').place(x=160, y=60)
        Entry(root, width = 70, textvariable = link).place(x = 32, y = 90)
        def VideoDownloader():
            url = YouTube(str(link.get()))
            video = url.streams.first()
            video.download()
            Label(root, text = "downloaded", font = "arial 15").place(x=180,y=210)
        Button(root, Text = "download", font = 'arial 15 bold', bg = 'pale violet red', padx = 2, command = VideoDownloader).place(x = 180, y = 150)
        root.mainloop()
        engine_talk('video downloaded')
        
    
    
    elif 'open notepad' in command:
        npath = 'C:\\WINDOWS\\system32\\notepad.exe'
        os.startfile(npath)
        engine_talk('opening notepad')
    

    elif 'open blue stack' in command:
        npath = 'C:\\Program Files\\BlueStacks_nxt.exe'
        os.startfile(npath)
        engine_talk('opening bluestack')


    elif 'activepresenter' in command:
        npath = 'C:\\Program Files\\ATOMI\\ActivePresenter.exe'
        os.startfile(npath)
        engine_talk('opening Active presenter')
    

    elif 'ip address' in command:
        ip = get('https://api.ipify.org').text
        engine_talk(f'your ip address is {ip}')
    
    
    elif 'alarm' in command:
        engine_talk('enter the time')
        time = input(": enter the time :")

        while True:
            Time_Ac = datetime.datetime.now()
            now = Time_Ac.strftime("%H:%M:%S")

            if now == time:
                engine_talk('time to wake up sir')
                playsound('Assistant.mp3.mp3')
                engine_talk('alarm closed')

            elif now>time:
                break

    
    elif 'google search' in command:
        import wikipedia as googleScrap
        command = command.replace("Assistant", "")
        command = command.replace("google search")
        command = command.replace("google", "")
        engine_talk('this is what i found on google')

        try:
            pywhatkit.search(command)
            result = googleScrap.summary(command, 1)
            engine_talk(result)
        except:
            engine_talk('No speakable data available!')

    
    
    elif 'wikipedia ' in command:
        engine_talk('searching wikipedia..........')
        result = wikipedia.summary(command, sentences=2)
        engine_talk('according to wikipedia')
        engine_talk(result)
        print(result)
    
    
    elif 'open google' in command:
        webbrowser.open('http://www.google.co.uk/')
        engine_talk('opening google')
    
    
    elif 'search on google' in command:
        engine_talk('sir, what should i search on google')
        cm = takecomand().lower()
        webbrowser.open(f"{cm}")
    
    
    elif 'what is my name' in command:
        engine_talk('your name is aditya')
    
    
    elif ' open comand prompt' in command:
        os.system("start cmd")
        engine_talk('opening comand prompt')
    
    
    elif ' cmd' in command:
        os.system("start cmd")
        engine_talk('opening cmd')
    
    
    elif 'send a message on whatsapp'in command:
        engine_talk('ok sir sending message')
        pywhatkit.sendwhatmsg('+918168205574', 'hi',14, 36)
        engine_talk('sir message has been sended')
    
    
    elif 'send a whatsapp message'in command:
        engine_talk('sending whatsapp message')
        pywhatkit.sendwhatmsg('+917015871479', 'hi', 23, 20)
        engine_talk('ok sir sending message')
    
    
    elif 'hello' in command:
        engine_talk('hello sir how may i help you sir')
    
    
    elif 'hi' in command:
        engine_talk('hi sir how may i help you sir')
    
    
    elif 'social media ' in command:
        engine_talk('which social media app may i open sir')
    
    
    elif 'who are you' in command:
        engine_talk('I am your personal assistant name assistant who work i will work on your voice command')
    
    
    elif 'what is your name' in command:
        engine_talk('my name is assistant who work i will work on your voice command ')
    
    
    elif 'month' in command:
        year = datetime.datetime.now().strftime('%m')
        engine_talk('month is' +year )
    
    
    elif 'date' in command:
        year = datetime.datetime.now().strftime('%d')
        engine_talk('day is' +year  )
    
    
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        engine_talk('The current time is' +time)
    
    
    elif 'who is' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        engine_talk (info)
    
    
    elif 'joke' in command:
        engine_talk(pyjokes.get_joke())
        print()


    elif 'language you' in command:
        engine_talk("i had made from python language, Python is an interpreted high-level general-purpose programming language. Its design philosophy emphasizes code readability with its use of significant indentation. Its language constructs as well as its object-oriented approach aim to help programmers write clear, logical code for small and large-scale projects.") 
    

    elif 'weather' in command:
        engine_talk('Please tell the name of the city')
        city = user_commands()
        #weather_api = weather('Hong Kong')
        weather_api = weather(city)
        engine_talk(weather_api + 'degree fahreneit' )
    
    
    elif 'sleep' in command:
        engine_talk('sleeping in 2 seconds,  2      ,        1       ')
        sys.exit()
    
    
    elif 'stop' in command:
        engine_talk('stoping in 2 seconds,  2        ,      1       ')
        sys.exit()
    

    elif 'rahul prank' in command:
        webbrowser.open('https://www.youtube.com/channel/UCbamlWa7ZvcVVPPFVPVBBaw/about')
        engine_talk('opening sir')

    elif 'himanshu prank' in command:
        webbrowser.open('https://www.youtube.com/channel/UCasX-wa39sqcj1oVXimdwfA')
        engine_talk('opening sir')
    
    elif 'gaurav ' in command:
        webbrowser.open('https://www.youtube.com/channel/UCRgMIwmmh1-2k5HeTQ2cdkQ')
        engine_talk('opening sir')

    elif 'movie explain' in command:
        webbrowser.open('https://www.youtube.com/channel/UCtxT50MzIRx0H2qdQYRoQeg')
        engine_talk('opening sir')






    elif 'quit' in command:
        engine_talk('quiting in 2 seconds,  2        ,      1       ')
        sys.exit()
    
    
    elif 'you need a break' in command:
        engine_talk('ok sir you can call me at any time going in 2 seconds,  2        ,      1       ')
        sys.exit()
    
    
    elif 'good night' in command:
        engine_talk('good night sir, have a sweet dreams')
        sys.exit()
    
    elif 'bye bye' in command:
        engine_talk('bye bye sir, have a great day')
        sys.exit()
    
    
    elif 'good morning' in command:
        engine_talk('good morning sir, let start our work')
    
    elif 'good evening' in command:
        engine_talk('good evening, lets have a fun')
    
    
    elif 'good afternoon' in command:
        engine_talk('good afternoon sir, lets have a fun')
    
    
    elif'no thanks' in command:
        engine_talk('thanks sir, i am happy have helped you, hava a nice day, bye bye!! ')
        sys.exit()




        engine_talk('sir do you have any other work')

    elif'no' in command:
        engine_talk('sorry sir, sorry')
        sys.exit()

    else:
        engine_talk('please tell the command again')


while True:
    run_alexa()

