# importing requests and json
import requests
from Features import sndisplay, speak

# Base URL
BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
API_KEY = "79d2d8607771cdfb10bef2ad37e6acde"


def get_weather(CITY):
    speak("Sure Sir, I am retrieving the weather information for " + CITY)
    URL = BASE_URL + "q=" + CITY + "&appid=" + API_KEY + "&units=metric"
    try:
        # HTTP request
        response = requests.get(URL)
        # checking the status code of the request
        # getting data in the json format
        data = response.json()
        # getting the main dict block
        main = data['main']
        # getting temperature
        temperature = main['temp']
        # getting the humidity
        humidity = main['humidity']
        # getting the pressure
        pressure = main['pressure']
        wind_speed = data['wind']['speed']
        report = data['weather']
        print(f"\n<{CITY.upper():-^30}>\n")
        print(f"Temperature: {round(temperature)}" + "°C")
        speak(f"Temperature is {round(temperature)}" + "°C")
        print(f"Humidity: {humidity}")
        speak(f"Humidity is {humidity}" + "Percent")
        print(f"Pressure: {round(pressure / 33.864, 2)}" + " inHg")
        speak(f"Air Pressure is {round(pressure / 33.864, 2)}" + " Inches of mercury")
        print(f"Visibility: {data['visibility'] / 1000}" + " Km")
        speak(f"Visibility is around {data['visibility'] / 1000}" + " Km")
        print(f"Wind Speed: {wind_speed}" + " Km/h")
        speak(f"The Wind Speed is {wind_speed}" + "Kilometers per hour")
        print(f"Weather Report: {report[0]['description']}")
    except Exception as e:
        # showing the error message
        if response.status_code != 200:
            sndisplay("Sorry Sir, I couldn't connect to the server because there might be an error in the HTTP request or the city name may not be correct")