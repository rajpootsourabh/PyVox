# importing important packages, libraries and modules
from Features import*
# from uims_login import uimsBot
# from Instagram import instaBot
from Weather import get_weather
from time import sleep


# <------------Main Code Starts from here------------>

if __name__ == '__main__':
    wishme("Mr. Singh")
    sndisplay("I'm your voice assistant")
    sndisplay("What can i do for you today?")

while True:
    # To take command from user as input
    query = takeCommand()

    if 'no thanks' in query or 'not' in query or 'nahi' in query or 'naa' in query:
        GreetOnExit()

    elif 'youtube' in query:
        key = query.replace("play song", "").replace("on youtube", "").replace("play music", "").replace("gaana chalao", "").replace("gana chalao", "")
        if song_name := str(key):
            pywhatkit.playonyt(song_name)
            sndisplay("Playing....")
        else:
            webbrowser.open("www.youtube.com")

    elif 'student portal' in query or 'uims' in query or 'chandigarh' in query:
        speak("Okay Sir, Just give me a momment ...")
        url = "https://uims.cuchd.in/uims/"
        file = open("E:\\Learn_Python\Pass_file.txt", "r")
        data = file.read()
        data = data.replace(": ", " ").replace("\n", " ")
        data = data.split(" ")
        # uimsBot(data[1], data[3], url)
        continue

    elif 'play music' in query or 'music' in query or 'gana chala' in query or 'gana baja' in query or 'play a song' in query:
        sndisplay("Ok Sir, please tell me the title of the song")
        name = takeCommand()
        play_music(name[:7])

    elif 'shutdown' in query or 'turn off' in query or 'goodnight' in query or 'sone ja' in query or 'good night' in query:
        if 'night' in query or 'sone' in query:
            speak("Sir, Are you going to sleep?")
            rep = takeCommand()
            if "y" in rep or "ha" in rep:
                speak("Okay, Sir as you told me that you are going to sleep so let me shutdown the system to save the battery")
            else:
                speak("Okay, Sir give me a moment to shutdown the system")
            shutdown_Sys(query)
        else:
            shutdown_Sys(query)


    elif 'open camera' in query or 'camera' in query:
        speak("Okay Sir, I'm opening Camera ...")
        os.system("start microsoft.windows.camera:")


    elif 'close' in query:
        py.keyDown('alt')
        py.press('f4')
        py.keyUp('alt')

    elif 'whatsapp message' in query or 'whatsapp' in query:
        # the statement inside 'if' will only be executed if a user speaks in hindi
        if 'ko' in query:
            lis = query.split(" ")
            name = lis[0]
            # whatsappMsg(name)
        else:
            lis = query.split(" ")
            name = lis[len(lis)-1]
            #whatsappMsg(name)

    elif 'instagram' in query or 'message on instagram' in query or 'insta' in query:
        file = open(f"D:\Learn_Python\Pass_file.txt", "r")
        data = file.read()
        data = data.replace(": ", " ").replace("\n", " ")
        data = data.split(" ")
        username = data[5]
        password = data[7]
        recipient = ['____abhishek____singh_____']
        sndisplay("Wha's the message for " +recipient[0])
        message = takeCommand()
        # function call
        # instaBot(username, password, recipient, message)

    elif 'on google' in query or 'on internet' in query or 'search on google' in query or 'search on internet' in query or 'google' in query:
        get_weather(query)

    elif 'switch the window' in query or 'switch window' in query:
        py.keyDown('alt')
        py.press('tab')
        sleep(1)
        py.keyUp('alt')

    elif 'where we are' in query or 'ham kahan hain' in query:
        curr_Location()

    elif 'battery' in query or 'charge' in query:
        batteryInfo()

    elif 'speed' in query or 'internet speed' in query:
        netSpeed()

    elif 'volume' in query or 'awaaz' in query or 'aawaz' in query:
        query = query.replace('%', "")
        times = [int(i) for i in query.split() if i.isdigit()]
        if len(times)>=1:
            sysVolume(query, int(times[0]))
        else:
            sysVolume(query, 25)

    elif 'instagram followers' in query:
        # speak("Please type the username:")
        # username = str(input('Username: '))
        # # calling scrape function
        # data = scrape_data(username)
        # sndisplay("Mr. "+username+" has "+str(data['Followers'])+" followers, and he follows "+str(data['Following'])+" people")
        pass

    elif 'brightness' in query:
        query = query.replace('%', "")
        time = [int(i) for i in query.split() if i.isdigit()]
        if len(time)>0:
            brightness_Ctrl(query, int(time[0]))
        else:
            brightness_Ctrl(query, 20)

    elif 'live video' in query or 'recording' in query or 'stream' in query:
        liveVideo()

    elif 'weather' in query or 'mausam' in query:
        speak("Okay Sir, Please tell me the city name")
        city = takeCommand()
        get_weather(city)

    elif 'you need a break' in query or 'aram' in query or 'aaram' in query:
        speak("Okay, sir i am going to sleep")
        speak("You can call me anytime")
        break
    # executed only if none of the above condition is satisfied
    # else:
    #     sndisplay("Sorry to say, but I don't know that")
    #     sndisplay("Try Something like...\n\"Open Google Chrome\" \n\"Play Music\"")
    #     query = takeCommand()
    #     continue