import pyttsx3
import speech_recognition as sr
import datetime
import os
import random
import webbrowser
import wikipedia
import pyjokes
import time
import subprocess
import pyautogui
import psutil
import winshell
import socket
import imdb
import pywhatkit
import sys
import requests
import json

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
uname = ""


# ---------------------------------------------------BEGIN OF USER DEFINED FUNCTION-------------------------------------#


# ----------------------------------BASIC SPEECH-TO-TEXT AND EXIT FUNCTION------------------------------------------------#
def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("\nListening.........")
        r.pause_threshold = 1
        try:
            audio = r.listen(source, timeout=5, phrase_time_limit=10)
            print("Recognizing....")
            query = r.recognize_google(audio, language='en-in')
            print(f"user said: {query}\n")
            return query.lower()
        except sr.WaitTimeoutError:
            speak("Unable to recognize your voice....")
            speak("Please tell me the command again,boss. You can tell me to exit to terminate my services.")
            return takeCommand()
        except sr.UnknownValueError:
            speak("Unable to recognize your voice....")
            speak("Please tell me the command again,boss. You can tell me to exit to terminate my services.")
            return takeCommand()
        except Exception as e:
            speak("An error occurred while processing your command.")
            speak("Please try again, boss. You can tell me to exit to terminate my services.")
            return takeCommand()


def exit():
    speak("Thanks for using me,boss. Have a good day")
    sys.exit()


def username():
    speak("Welcome boss")
    speak("What should I call you?")
    uname = takeCommand()
    if (uname == "exit"):
        return exit()
    else:
        speak("Hi " + uname)
        speak("How can I help you today boss?")


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning Boss" + uname)
    elif hour >= 12 and hour < 16:
        speak("Good Afternoon Boss" + uname)
    else:
        speak("Good Evening Boss" + uname)
    speak("I am your virtual assistant Emma")


# ----------------------------------CPU FUNCTION------------------------------------------------#
def cpu():
    usage = str(psutil.cpu_percent())
    speak("CPU is at " + usage)
    battery = str(psutil.sensors_battery())
    speak("Battery is at " + battery)


# -------------------------------------------   HOW ARE YOU FUNCTION ------------------------------------------------#
def howareyou():
    speak("I am fine, Thank you.")
    speak("How are you,boss?")
    order = takeCommand().lower()
    if any(word in order for word in ['happy', 'fine', 'contented', 'good', 'okay', 'better', 'ok']):
        speak("It's good to know that you are fine.")
        speak("How can I help you today boss.")
    elif any(word in order for word in ['depressed', 'sad', 'lonely', 'dying', 'killing myself', 'suicide', 'low']):
        speak("I'm sorry to hear that you're feeling this way.")
        speak("Remember, you don't have to face it alone. Reach out to your loved ones or seek professional help.")
        speak("I am always here for you. You can tell me to play a song on youtube to cheer you up.")
    elif any(word in order for word in ['angry', 'frustrated', 'annoyed', 'irritated', 'agitated']):
        speak("I'm sorry to hear that you're feeling this way.")
        speak(
            "Remember, you don't have to face it alone. Reach out to your loved ones and speak about whats bothering you.")
        speak("I am always here for you. You can tell me to play a song on youtube to cheer you up.")
    else:
        speak("I am sorry but I didnt understand that. Please give me another command Boss")


# ----------------------------------GOOGLE FUNCTION------------------------------------------------#
def google(order):
    try:
        query = order  # true variable whhich will be searched on google exactly
        words_to_remove = ('emma', 'find', 'on google', 'google search', 'search', 'open')
        for word in words_to_remove:
            query = query.replace(word, "")
            query = query.strip()  # Remove leading/trailing spaces
        if 'open' in order or 'find' in order:
            speak('opening ' + query + ' on google.')
        else:
            speak('searching ' + query + ' on google.')
        query_words = query.split()  # Split query into individual words
        query = '+'.join(query_words)  # Join words with plus symbols in between
        pywhatkit.search(query)
        result = wikipedia.summary(order, sentences=1)
        speak(result)

    except:
        query = order
        speak("I am sorry,but i didnt get that.Please tell the exact words to search on google")
        query_words = query.split()  # Split query into individual words
        query = '+'.join(query_words)  # Join words with plus symbols in between
        pywhatkit.search(query)
        result = wikipedia.summary(order, sentences=1)
        speak(result)


# ----------------------------------YOUTUBE FUNCTION------------------------------------------------#
def youtube(order):
    try:
        query = order
        words_to_remove = ('emma', 'play', 'on youtube', 'youtube search', 'search', 'open')
        for word in words_to_remove:
            query = query.replace(word, "")
            query = query.strip()  # Remove leading/trailing spaces
        if 'open' in order or 'search' in order:
            speak('opening ' + query + ' on youtube.')
        else:
            speak('playing ' + query + ' on youtube.')
        query = query.strip()  # Remove leading/trailing spaces
        query_words = query.split()  # Split query into individual words
        query = '+'.join(query_words)  # Join words with plus symbols in between
        web = "https://www.youtube.com/results?search_query=" + query
        webbrowser.open(web)
        pywhatkit.playonyt(order)
    except:
        query = order
        speak("I am sorry,but i didnt get that.Please tell the exact words to search")
        web = "https://www.youtube.com/results?search_query=" + query
        webbrowser.open(web)
        pywhatkit.playonyt(order)


# ----------------------------------AMAZON FUNCTION------------------------------------------------#
def amazon(order):
    try:
        query = order
        words_to_remove = ('emma', 'play', 'on amazon', 'amazon search', 'search', 'open', 'find')
        for word in words_to_remove:
            query = query.replace(word, "")
            query = query.strip()  # Remove leading/trailing spaces
        if 'open' in order or 'search' in order:
            speak('opening ' + query + ' on amazon.')
            speak('Happy shopping')
        else:
            speak('searching ' + query + ' on amazon.')
            speak('Happy shopping')
        query = query.strip()  # Remove leading/trailing spaces
        query_words = query.split()  # Split query into individual words
        query = '+'.join(query_words)  # Join words with plus symbols in between
        web = "https://www.amazon.com/s?k=" + query
        webbrowser.open(web)
    except:
        query = order
        speak("I am sorry,but i didn't get that.Please tell the exact words to search on amazon")
        web = "https://www.amazon.com/s?k=" + query
        webbrowser.open(web)


# -----------------------------------------------  FLIPKART FUNCTION  --------------------------------------------------#
def flipkart(order):
    try:
        query = order
        words_to_remove = ('emma', 'play', 'on flipkart', 'flipkart search', 'search', 'open')
        for word in words_to_remove:
            query = query.replace(word, "")
            query = query.strip()  # Remove leading/trailing spaces
        if 'open' in order or 'search' in order:
            speak('opening ' + query + ' on flipkart.')
            speak('Happy shopping')
        else:
            speak('searching ' + query + ' on flipkart.')
            speak('Happy shopping')
        query = query.strip()  # Remove leading/trailing spaces
        query_words = query.split()  # Split query into individual words
        query = '+'.join(query_words)  # Join words with plus symbols in between
        web = "https://www.flipkart.com//search?q" + query
        webbrowser.open(web)

    except:
        query = order
        speak("I am sorry,but i didnt get that.Please tell the exact words to search")
        web = "https://www.flipkart.com//search?q" + query
        webbrowser.open(web)


def healthQuery(query):
    if 'symptoms' in query:
        # Call an API to get information about symptoms
        response = requests.get('API_ENDPOINT', params={'query': query})
        data = json.loads(response.text)
        if 'result' in data:
            symptoms = data['result']
            speak(f"The common symptoms for {query} are: {', '.join(symptoms)}")
        else:
            speak("I'm sorry, I couldn't find information about the symptoms.")
    elif 'calculate bmi' in query:
        speak("Sure, please provide your height and weight.")
        height = float(takeCommand())
        weight = float(takeCommand())
        bmi = weight / ((height / 100) ** 2)
        speak(f"Your BMI is {bmi:.2f}.")
        if bmi < 18.5:
            speak("You are underweight.")
        elif 18.5 <= bmi < 25:
            speak("You are in the normal weight range.")
        elif 25 <= bmi < 30:
            speak("You are overweight.")
        else:
            speak("You are obese.")
    elif 'heart rate' in query:
        # Call an API to measure heart rate (e.g., using a wearable device)
        heart_rate = get_heart_rate()
        speak(f"Your current heart rate is {heart_rate} beats per minute.")
    elif 'blood pressure' in query:
        # Call an API to measure blood pressure (e.g., using a blood pressure monitor)
        systolic_pressure, diastolic_pressure = get_blood_pressure()
        speak(f"Your current blood pressure is {systolic_pressure}/{diastolic_pressure} mmHg.")
    else:
        speak("I'm sorry, I don't have information about that health query.")


def exit():
    speak("Thanks for using me, boss. Have a good day")
    sys.exit()


# ------------------------------------------------  CHATGPT-------------------------------------------------------------#
# -----------------------------------------------   WHATSAPP -----------------------------------------------------------#
# ----------------------------------------------- WIKIPEDIA FUNCTION  -------------------------------------------------#
# ----------------------------------------------  GOOGLE MAPS FUNCTION-------------------------------------------------#
# ----------------------------------------------  MYNTRA FUNCTION------------------------------------------------------#
# ----------------------------------------------  INSTAGRAM FUNCTION---------------------------------------------------#
# ----------------------------------------------  TWITTER FUNCTION-----------------------------------------------------#


# ---------------------------------------END OF USER DEFINED FUNCTIONS-------------------------------------------------#


# ----------------------------------------------    MAIN FUNCTION-------------------------------------------------------#
if __name__ == '__main__':
    wishMe()
    username()
    while True:
        order = takeCommand().lower()
        # ---------------------------------  GENERAL CONVERSATION----------------------------------#
        if 'how are you' in order:
            howareyou()

        elif 'who am i' in order:
            speak("If you can talk, then surely you are a human.")

        elif 'who are you' in order:
            speak("I am your virtual assistant Emo.")

        elif 'i love you' in order:
            speak("Oh my god, thank you. I love you too. Anything I can help you with?")

        elif 'will you be my girlfriend' in order or 'will you be my valentine' in order:
            speak("I'm not sure about that, maybe you should give me some more time.")

        elif 'will you be my boyfriend' in order or 'will you be my valentine' in order:
            speak("I'm not sure about that, maybe you should give me some more time.")

        elif "what is your name" in order or "what's your name" in order or "tell me your name" in order:
            speak("My friends call me Emma.")

        elif 'love' in order:
            speak("Love is the 7th sense that detroys all other senses")

        elif 'joke' in order:
            speak(pyjokes.get_joke(language="en", category="neutral"))

        elif 'the time' in order:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Well, the time is {strTime}")

            # ------------------------------ ACCESS FUNCTIONS -----------------------------------------#

        elif "write a note" in order:
            speak("What should I write?")
            note = takeCommand()
            file = open('jarvis.txt', 'w')
            speak("boss, should I include date and time as well?")  # ---------WRITE A NOTE--------#
            sn = takeCommand()
            if 'yes' in sn or 'sure' in sn or 'yeah' in sn:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                file.write(strTime)
                file.write(note)
                speak("Done boss!")
            else:
                file.write(note)
                speak("Done boss!")

        elif 'show note' in order:
            speak("Showing notes")
            file = open("jarvis.txt", "r")  # ---------SHOW NOTE--------#
            print(file.read())
            speak(file.read(6))



        elif 'open notepad' in order:
            speak("Opening Notepad.")  # ---------NOTEPAD--------#
            npath = "C:\\Windows\\system32\\notepad.exe"
            os.startfile(npath)

        elif 'open photoshop' in order:
            npath = "C:\\Program Files\\Adobe\\Adobe Photoshop 2020\\photoshop.exe"  # ---------PHOTOSHOP--------#
            os.startfile(npath)

        elif 'play music' in order or 'play songs' in order:
            music_dir = "E:\\Songs\\New folder"
            songs = os.listdir(music_dir)  # ---------MUSIC--------#
            rd = random.choice(songs)
            os.startfile(os.path.join(music_dir, rd))

        elif 'wikipedia' in order:
            speak('Searching......')
            order = order.replace("wikipedia", "")  # ---------WIKIPEDIA---------#
            results = wikipedia.summary(order, sentences=1)
            speak("According to Wikipedia")
            speak(results)

        elif 'open google' in order:
            speak("Here you go to Google \n")  # ---------GOOGLE--------#
            webbrowser.open("https://google.co.in")

        elif 'google' in order:
            google(order)  # ---------GOOGLE SEARCH--------#

        elif 'open youtube' in order:
            speak("Here you go to YouTube \n")
            webbrowser.open("https://youtube.com")

        elif 'youtube' in order:
            youtube(order)

        elif 'open myntra' in order:
            speak("Here you go to Myntra, boss. Happy shopping \n")
            webbrowser.open("www.myntra.com")

        elif 'open amazon' in order:
            speak("Here you go to Amazon,boss. Happy shopping")
            webbrowser.open("www.amazon.in")

        elif 'amazon' in order:
            amazon(order)

        elif 'open flipkart' in order:
            speak("Here you go to flipkart,boss. Happy shopping")
            webbrowser.open("www.flipkart.in")

        elif 'flipkart' in order:
            flipkart(order)

        elif 'google maps' in order:
            order = order.replace("where is ", "")
            location = order
            speak("Locating....")
            speak(location)
            webbrowser.open("https://www.google.co.in/maps/place/" + location + "")

        elif 'open stackoverflow' in order:
            speak("Here you go to Stack Overflow. Happy coding")
            webbrowser.open("www.stackoverflow.com")

        elif 'open chatgpt' in order:
            speak("opening chatgpt")
            webbrowser.open("https://chat.openai.com/")


        # --------------------------------------- SYSTEM FUNCTIONS ---------------------------------------------------#

        elif 'shutdown' in order or 'turn off' in order:
            speak('Hold on a second boss! Your system is on its way to shutdown')
            speak('Make sure all of your applications are closed')
            time.sleep(5)
            subprocess.call(['shutdown', '/s'])

        elif 'restart' in order:
            speak('Restarting.....')
            subprocess.call(['shutdown', '/r'])

        elif 'hibernate' in order:
            speak("Hibernating.....")
            subprocess.call(['shutdown', '/h'])

        elif 'log off' in order or 'sign out' in order:
            speak('Make sure all of your applications are closed before signing out, boss!')
            time.sleep(5)
            subprocess.call(['shutdown', '/i'])

        elif 'switch window' in order:
            pyautogui.keyDown('alt')
            pyautogui.press('tab')
            time.sleep(1)
            pyautogui.keyUp('alt')

        elif 'take a screenshot' in order or 'screenshot this' in order:
            speak('boss, please tell me the name for this file.')
            name = takeCommand().lower()
            speak("Please hold the screen")
            time.sleep(3)
            img = pyautogui.screenshot()
            img.save(f"{name}.png")
            speak("Screenshot captured, boss!")

        elif 'cpu status' in order:
            cpu()

        elif 'empty recycle bin' in order:
            winshell.recycle_bin().empty(confirm=False, show_progress=False, sound=True)
            speak("Recycle bin recycled")



        elif 'exit' in order or 'quit' in order or '':
            speak("Thanks for using me,boss. Have a good day")
            sys.exit()

        elif 'ip' in order:
            host = socket.gethostname()
            ip = socket.gethostbyname(host)
            speak("Your IP address is " + ip)
        # ------------------------------ BMI -----------------------------------------#
        elif 'bmi' in order:
            speak("Please tell your height in centimeters")
            height = takeCommand()
            speak("Please tell your weight in kilograms")
            weight = takeCommand()
            height = height / 100
            BMI = weight / (height * height)
            speak("Your body mass index is " + str(BMI))
            if BMI > 0:
                if BMI <= 16:
                    speak("You are severely underweight")
                elif BMI <= 18.5:
                    speak("You are underweight")
                elif BMI <= 25:
                    speak("You are healthy")
                elif BMI <= 30 and BMI <= 35:
                    speak("You are overweight")
                else:
                    speak("You are severely overweight")
            else:
                speak("Enter valid details")
        # ------------------------------ MOVIE FUNCTIONS -----------------------------------------#
        elif 'movie' in order:
            moviesdb = imdb.IMDb()
            speak("Please tell me the movie name, boss")
            text = takeCommand()
            movies = moviesdb.search_movie(text)
            speak("Searching for " + text)
            if len(movies) == 0:
                speak("No results found")
            else:
                speak("I found these:")
                for movie in movies:
                    title = movie["title"]
                    year = movie["year"]
                    speak(f'{title} ({year})')
                    info = movie.getID()
                    movie = moviesdb.get_movie(info)
                    rating = movie['rating']
                    plot = movie['plot outline']
                    if year < int(datetime.datetime.now().strftime("%Y")):
                        speak(
                            f'{title} was released in {year} and had IMDB rating of {rating}. The plot summary of the movie is {plot}')
                        break
                    else:
                        speak(
                            f'{title} will be released in {year} and had IMDB rating of {rating}. The plot summary of the movie is {plot}')
                        break



        # Handle health-related queries
        elif 'health' in order or 'medical' in order:
            healthQuery(order)


        # ------------------------------ DEFAULT FUNCTIONS -----------------------------------------#
        else:
            speak(
                "I am sorry to say that I cannot perform that. Please give me another command boss. You can tell exit to terminate my services")


