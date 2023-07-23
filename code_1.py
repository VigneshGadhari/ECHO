#Importing Neccesary modules
import requests
from shutil import copyfileobj
import speech_recognition as sr
import pyttsx3
import datetime
from datetime import date
from datetime import timedelta
import os
os.system("color 70")

'''
  ____                       _                                _       _ _   _             
 / ___| _ __   ___  ___  ___| |__    _ __ ___  ___ ___   __ _(_)_ __ (_) |_(_) ___  _ __  
 \___ \| '_ \ / _ \/ _ \/ __| '_ \  | '__/ _ \/ __/ _ \ / _` | | '_ \| | __| |/ _ \| '_ \ 
  ___) | |_) |  __/  __/ (__| | | | | | |  __/ (_| (_) | (_| | | | | | | |_| | (_) | | | |
 |____/| .__/ \___|\___|\___|_| |_| |_|  \___|\___\___/ \__, |_|_| |_|_|\__|_|\___/|_| |_|
       |_|                                              |___/                             
'''
listener = sr.Recognizer() #Listener for the speech recoginition module
engine = pyttsx3.init() #Engine for Pythontts
voices = engine.getProperty('voices') #get a property called voice form the sr module
engine.setProperty('voice', voices[1].id) #Set the properties of the voice


f = open("User.txt", "r") #User command file
g = open("Reply.txt","r")#The reply of the Voice Assistant
list2 = g.readlines()

def speak(message):
    engine.say(message)
    engine.runAndWait()


def mic(): #According to Background noise it changes.
    print("Echo:Listening...")
    voice = listener.listen(source) #the listener will listen to the source
    v = listener.recognize_google(voice) #To convert the speech to using google api
    
    return v


'''
     _    ____ ___ 
    / \  |  _ \_ _|
   / _ \ | |_) | | 
  / ___ \|  __/| | 
 /_/   \_\_|  |___|
'''
def movie_info():
    import requests
    print("Echo:Please name the movie")
    speak("Please name the movie")
    title = mic()
    print("\tYou:"+title.capitalize())
    api_key = '12768673'
    url = f'http://www.omdbapi.com/?apikey={api_key}&'
    params = {'t': title, 'j': 'json'}
    r = requests.get(url, params=params)

    mi = r.json()
    if mi['Response'] == 'True':
        for item in mi['Ratings']:
            items = item['Source']+' - '+item['Value']
        print("Echo:\n"+"-------------------------Title-------------------------")
        print(mi['Title'])
        print("-------------------------Info--------------------------")
        reply = f'''Released: {mi['Released']}\nRated: {mi['Rated']}\nRuntime: {mi['Runtime']}\nGenre:{mi['Genre']}\nDirector: {mi['Director']}\nActors: {mi['Actors']}\nLanguage: {mi['Language']}\nRatings:{items}\nPlot: {mi['Plot']}''' 
        pst = f'''Poster: {mi['Poster']}'''
        print("\n"+reply)
        print(pst)
        speak(reply)
    else:
        print("Echo:Movie not found")
        speak("Movie not found")

def wolfarmapla_api():
    import wolframalpha
    try:
        print("Echo:Please ask your question")
        speak("Please ask your question")
        query = mic()
        print(f"\tYou: "+query.capitalize())
        speak(f"Your Question: {query}")
        app_id = '5VXEXE-GEE2YQLGG8'
        client = wolframalpha.Client(app_id)
        res = client.query(query)
        answer = next(res.results).text
        print("Echo:"+answer)
        speak(answer)
    except:
        print("Echo:Invalid Question")
        speak("Invalid Question") 
def coronavirus_update():

    url = "https://covid-193.p.rapidapi.com/history"

    print("Please provide the country name")
    speak("Please provide the country name")
    query = mic()
    print(f"\tYou: "+query.capitalize())
    yesterday = date.today() - timedelta(days = 1)
    querystring = {"country": query, "day":yesterday}

    headers = {
	    "X-RapidAPI-Key": "1a1101a099mshf99b6ddbf2bbc93p1e06ecjsn1c5fe4505e46",
	    "X-RapidAPI-Host": "covid-193.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)
    
    try:
        r = response.json()
        print("Country:",(r['parameters']['country']).capitalize())
        speak("Country")
        
        print("Day:",r['parameters']['day'])
        speak("Day")

        print("Population:",r['response'][2]['population'])
        speak("Population")

        print("Cases:\nNew:",r['response'][0]['cases']['new'])
        speak("cases")
        speak("New")

        print("Active:",r['response'][0]['cases']['active'])
        speak("Active:")

        print("Critical:",r['response'][0]['cases']['critical'])
        speak("Critical")

        print("Recovered:",r['response'][0]['cases']['recovered'])
        speak("Recovered")

        print("Deaths:",r['response'][0]['deaths']['total'])
        speak("Deaths")

        print("Total:",r['response'][0]['cases']['total'])
        speak("Total")
    except:
        print("Country not found")
        speak('Country not found')



'''
  __  __       _                       _      
 |  \/  | __ _(_)_ __     ___ ___   __| | ___ 
 | |\/| |/ _` | | '_ \   / __/ _ \ / _` |/ _ \
 | |  | | (_| | | | | | | (_| (_) | (_| |  __/
 |_|  |_|\__,_|_|_| |_|  \___\___/ \__,_|\___|
                                              
'''
print(
"""
___________________________________ 
|                           █    | 
|                            █   | 
|                         █   █  | 
|  █▀▀ █▀▀ █░░█ █▀▀█   █   █   █ | 
|  █▀▀ █░░ █▀▀█ █░░█    █  █   █ | 
|  ▀▀▀ ▀▀▀ ▀░░▀ ▀▀▀▀   █   █   █ | 
|                         █   █  | 
|                            █   | 
|                           █    | 
\u203E\u203E\u203E\u203E\u203E\u203E\u203E\u203E\u203E\u203E\u203E\u203E\u203E\u203E\u203E\u203E\u203E\u203E\u203E\u203E\u203E\u203E\u203E\u203E\u203E\u203E\u203E\u203E\u203E\u203E\u203E\u203E\u203E\u203E\u203E """)


while True:
    try:
        with sr.Microphone() as source: #mic = source
            listener.adjust_for_ambient_noise(source,duration=1)
            print("\nEcho:How may i help you?")
            speak("How may i help you")
            st = mic()
            print("\tYou:"+st.capitalize())
            if "coronavirus updates" in st:#Covid-Updates
                coronavirus_update()

            elif "movie information" in st:
                movie_info()

            elif "question" in st:
                wolfarmapla_api()    
            
            elif 'bye' in st:
                print("Echo:Have a great day!")
                speak("Have a great day")
                break       

            else:
                index = 0
                ans = ""
                for line in f: 
                    if st in line: #Searching for the string at a particular line in the command file
                        ans = list2[index]
                        break
                    index += 1
                if ans == "":
                    print("Echo:Invalid Question")
                    speak("Invalid Question")
                else:
                    print("Echo: "+ans)
                    speak(ans)
    except:
        print("Echo:Failed recognizing your voice")
        speak("Failed recognizing your voice")

