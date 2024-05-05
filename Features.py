# query-to-speech conversion library
# to open Application Software
# from AppOpener import run
# To check system information (e.g. battery info)
from psutil import sensors_battery
# for manipulating date and time
import datetime
# To work with json data
import json
# module to interact with operating system
import os
# to generate random number
import random
# URL handling module
import urllib.request
# web browser controller
import webbrowser
# for image processing
import cv2
# To work arrays
import numpy as np
# To control keyboard and mouse buttons
import pyautogui as py
import pyttsx3 as tts3
# whatsapp module
import pywhatkit
# To requests from server
import requests
# Importing the module
import screen_brightness_control as sbc
# speech recognition library
import speech_recognition as sr
# Check internet speed
import speedtest
# To generate fake user agent
from user_agent import generate_user_agent

# <******************************** Functions starts from here ********************************>

# 1- Using system voice to speak
engine = tts3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[4].id)
engine.setProperty('rate', 200)

# 2- Method to speak from query
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# 3- Taking input through from microphone r.pause_threshold =1
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        # r.adjust_for_ambient_noise(source, duration=3)
        r.pause_threshold = 1
        # print("Try Asking ...\n")
        audio = r.listen(source, timeout=5, phrase_time_limit=10)

    try:
        # print("Just wait\n")
        # print("Recognizing ...\n")
        query = r.recognize_google(audio, language='en-in')
        print(f"You : {query.capitalize()}\n")

    except Exception as e:
        # sndisplay("Sorry, Can you repeat that?")
        return "null"
    return query.lower()


# 4- This Method is called on startup
def wishme(name=""):
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning "+name)
    elif hour>=12 and hour<18:
        speak("Good Afternoon "+name)
    else:
        speak("Good Evening "+name)

# 5- To display and speak the command
def sndisplay(query):
    print("AI : "+query+"\n")
    speak(query)


# 6- Message on Program Termination
def GreetOnExit():
    hour = int(datetime.datetime.now().hour)
    val1 = random.randint(1, 4)
    if val1 == 1 and hour >= 20 and hour <= 23:
        speak("Okay Bye, Good Night, Sweet Dreams")
    elif val1 == 2:
        speak("You're welcome, I hope I could help you...")
    elif val1 == 3:
        speak("Okay Bye, I hope We will meet again")
    print("*<----You're Welcome---->*")
    exit()


# 7- Method to remove whitespaces and add country code in phone number
def add_countryCode(num):
    cc = "+91"
    mob = num.replace(" ", "")
    mobwcc = cc+mob
    return mobwcc


# 8- To match name with mobile number and save new no to the database
# file1 = open("NumberDB.txt", "r")
# Lines = file1.readlines()
# def phoneMatch(name):
#     for line in Lines:
#         if line.__contains__(name) == True:
#             new = line.replace(":", "").replace("-", "")
#             lis = new.split()
#             i = lis.index(name)+1
#             if lis[i].isdigit() == True:
#                 return lis[i]
#         else:
#             continue
#     sndisplay("Sorry, "+name+" is not in your contact list")
#     sndisplay("Would you like to save the number for "+name.title()+"?")
#     query = takeCommand()
#     if 'yes' in query or 'ha' in query or 'yeah':
#         sndisplay("Okay Sir, Please tell me the number you wanna save ...")
#     return "none"
#

# 9- Method to Confirm mobile no before sending msg
def confirm_Mob(mob):
    sndisplay("Do you want to proceed with "+mob)
    cnf = takeCommand()
    if 'yes' in cnf or 'ha' in cnf or 'haa' in cnf:
        return "True"
    else:
        return "False"

# 10- Method to check whether command is empty or not
# def getSuccess():
#     flag = 0
#     while flag < 3:
#         flag += 1
#         query = takeCommand()
#         if query != "null":
#             return str(query)
#     sndisplay("I am very Sorry, I could understand you")
#     sndisplay("It may be because of too much noise at your end")
#     GreetOnExit()
#     return 'none'

# 11- Function to remove spaces
def rm_spaces():
    query = takeCommand()
    res = query.replace(" ", "")
    return str(res)

# 12- To know the current location
def curr_Location():
    try:
        Access_Key = "3a9880a7c1e0597072f5d12ba89d1108"
        send_url = "http://api.ipstack.com/check?access_key=" +Access_Key
        geo_req = requests.get(send_url)
        geo_json = json.loads(geo_req.text)
        city = geo_json['city']
        sndisplay("I believe we are currently located in " + city.upper())
    except Exception:
        speak("I apologize, sir, but I'm currently experiencing a network issue, and as a result, I am unable to determine our current location.")

# 13- To control system volume

def sysVolume(query, percentage):
    if 'increase' in query or 'badha' in query:
        py.press('volumeup', presses=percentage)
        sndisplay(f"Okay, sir. I have increased the system volume by {percentage} percent.")
    elif 'decrease' in query or 'ghata' in query or 'kam' in query:
        py.press('volumedown', presses=percentage)
        sndisplay(f"Okay, sir. I have decreased the system volume by {percentage} percent.")
    elif 'full' in query:
        py.press('volumeup', presses=50)
        sndisplay("Okay, sir. I have set the system volume to the maximum.")
    elif 'mute' in query:
        py.press('volumemute')
        sndisplay("Okay, sir. I have muted the system volume.")
    elif 'unmute' in query:
        py.press('volumeunmute')
        sndisplay("Okay, sir. I have unmuted the system volume.")

# 14- To ShutDown the System
def shutdown_Sys(query):
    cmd = "shutdown /s"
    sec = [int(i) for i in query.split() if i.isdigit()]
    if len(sec)>0:
        speak("Ok, Shutting down System in "+str(sec[0])+" seconds")
        cmd = cmd+" "+str(sec)
        os.system(cmd)
        GreetOnExit()
    else:
        sndisplay("Shutting down the System ...")
        os.system(cmd)
        GreetOnExit()

# 15- To Control screen brightness
def brightness_Ctrl(query, n):
    # get current brightness value
    curr_brightness = sbc.get_brightness()
    if 'increase' in query or 'badh'in query:
        sbc.set_brightness(curr_brightness[0]+n)
        curr_brightness = sbc.get_brightness()
        sndisplay("Brightness has been increased and now set to "+str(curr_brightness[0])+"%")
    elif 'decrease' in query or 'ghata' in query or 'kam' in query:
        sbc.set_brightness(int(curr_brightness[0])-n)
        curr_brightness = sbc.get_brightness()
        sndisplay("Brightness has been deccreased and now set to " +str(curr_brightness[0])+ "%")


# 16(a) Play Local music
music_dir = 'D:\\Music & Videos\\New folder'
songs = os.listdir(music_dir)

def match_song(s_name):
    print(f"Your music directory contains a total of {str(len(songs))} songs\n")
    for song in songs:
        if s_name in str(song.lower()):
            return int(songs.index(song))
        else:
            continue
    return "none"

# 16(b) Play Local music
def play_music(s_name):
    index = match_song(s_name)
    if index != "none":
        os.startfile(os.path.join(music_dir, songs[index]))
    else:
        sndisplay("Sorry Sir, I can't play the request song")
        speak("It is possible that the song does not exist in the specified directory")
        speak("But don't worry, I still have a song for you")
        sndisplay("would you like to try other songs on the playlist?")
        cmd = takeCommand()
        if 'yes' in cmd or 'ha' in cmd or 'ya' in cmd:
            speak("Okay, I really hope you enjoy this song")
            i = random.randrange(0, len(songs))
            os.startfile(os.path.join(music_dir, songs[i]))
        else:
            speak("Okay, Is there anything else I can help you with?")


# 17- To Send whatsapp message
# def whatsappMsg(name):
#     sndisplay(f"Okay Sir, What is the message for {name.capitalize()}")
#     msg = takeCommand()
#     # ---Matching mob number with the database---#
#     db_result = phoneMatch(name)  # function call
#     mob = ""  # Initialing with Null value
#     if db_result == "none":
#         Mobile = rm_spaces()
#         if confirm_Mob(Mobile) == "True":
#             mob = str(add_countryCode(Mobile))
#             data = ["\n" + name + ": ", Mobile]
#             with open("Project\\VOICE ASSISTANT\\NumberDB.txt", 'a') as file1:
#                 file1.writelines(data)
#         else:
#             GreetOnExit()
#     else:
#         mob = str(add_countryCode(db_result))
#     pywhatkit.sendwhatmsg_instantly(mob, msg)


# 18- To Check internet speed


def checkInternetSpeed():
    speak("Certainly, sir. I'll check your internet speed now. Please wait for a moment.")
    try:
        # Creating a Speedtest object to measure internet speed
        st = speedtest.Speedtest()

        # Obtaining download and upload speeds
        download_speed = st.download()
        upload_speed = st.upload()

        # Converting speeds to megabytes per second and rounding to two decimal places
        formatted_download_speed = round(download_speed / 1048576 * 0.125, 2)
        formatted_upload_speed = round(upload_speed / 1048576 * 0.125, 2)

        # Displaying the results to the user
        sndisplay(f"Your Download Speed is {formatted_download_speed} Megabit Per Second.")
        sndisplay(f"Your Upload Speed is {formatted_upload_speed} Megabit Per Second.")
    except Exception as e:
        # Informing the user about the inability to check internet speed
        sndisplay("I apologize, but I'm currently unable to check your internet speed. Please try again later.")

    # Example usage:
    checkInternetSpeed()


# 19- Search on Google
def googleSearch(query):
    s_term = query.replace("search on google", "").replace("search on internet", "").replace("over internet", "")
    base_url = "https://www.google.com/search?q="
    URL = base_url + s_term
    webbrowser.open(URL)


# 20- For information about system battery
def batteryInfo():
    sensor = sensors_battery()
    battPer = sensor.percent
    charStat = sensors_battery().power_plugged
    if charStat:
        print(f"Battery Status : {battPer}" + "% available")
        print(f"Charger : Plugged in")
        speak("Your System has " + str(battPer) + " Percentage of Battery and you devices is being chargerd")
    else:
        print(f"Battery Status : {battPer}" + "% available")
        print(f"Charger : Unplugged")
        speak("Your System has " + str(battPer) + " Percentage of Battery")

# generating fake user agent
def user_Agent():
    userAgent = ""
    while True:
        userAgent = generate_user_agent()
        if 'compatible' in userAgent:
            continue
        else:
            break
    return userAgent


# Live video streaming using smartphone
# _____________Needs to be improved_____________
def liveVideo():
    URL = "http://192.168.197.220:8080///shot.jpg"
    while True:
        img_arr = np.array(bytearray(urllib.request.urlopen(URL).read()), dtype=np.uint8)
        img = cv2.imdecode(img_arr, 1)
        cv2.imshow('IPWebcam', img)
        # q = cv2.waitKey(1)
        q = takeCommand()
        if q == "close":
            break
    cv2.destroyAllWindows()


