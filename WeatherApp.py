"""We will build a weather app using Tkinter from Python"""
"""Developer Thomas Zelaya"""

# Import all the functions that will be needed
from tkinter import *
import requests
import json
from datetime import datetime

# We will now initialize the window
root = Tk()
root.geometry("400x400")  # this is the size of the window
root.resizable(0, 0)  # to make the window fixed
root.title("Weather App ")  # The title of our application

"""Now we will grab the data to be used in our app from OpenWeatherMap API"""
# My API keys from OWM: 5af879bb813fd9d3c253d91ea91c28be

"""Creating the weather function for the app"""
city_value = StringVar()


def showWeather():
    """Function to display the weather"""
    # We will now enter the API keys from the app we copied
    api_key = "5af879bb813fd9d3c253d91ea91c28be"

    city_name = city_value.get()  # this will be the input of the city name given to us

    # ADD the API url below
    weather_url = 'http://api.openweathermap.org/data/2.5/weather?q=' + city_name + '&appid=' + api_key

    response = requests.get(weather_url)  # get the response from the url

    weather_info = response.json()  # changing the response from json to python

    tfield.delete("1.0", "end")  # this clears the text field for every new ouput

    if weather_info['cod'] == 200:
        kelvin = 273  # value of kelvin

        # --------- storing the fetched values from weather of the city
        temp = int(weather_info['main']['temp'] - kelvin)
        feels_like_temp = int(weather_info['main']['feels_like'] - kelvin)
        pressure = weather_info['main']['pressure']
        humidity = weather_info['main']['humidity']
        wind_speed = weather_info['wind']['speed'] * 3.6
        sunrise = weather_info['sys']['sunrise']
        sunset = weather_info['sys']['sunset']
        timezone = weather_info['timezone']
        cloudy = weather_info['clouds']['all']
        description = weather_info['weather'][0]['description']

        sunrise_time = time_format_for_location(sunrise + timezone)
        sunset_time = time_format_for_location(sunset + timezone)

        # assign values to weather varaible to display output
        weather = f"\Weather of: {city_name}\nTemperature (Celsius): {temp}\nFeels like in (Celsius): {feels_like_temp}" \
                  f"\Pressure: {pressure}\nHumidity: {humidity}%\nSunrise at {sunrise_time} and Sunset at {sunset_time} " \
                  f"\nCloud: {cloudy}%\nInfo: {description}"
    else:
        weather = f"\n\tWeather for '{city_name}' not found!\n\tKindly Enter a valid City Name!"

    tfield.insert(INSERT, weather)  # insert or send value in our text field to display output


def time_format_for_location(utc_with_tz):
    """this function will change the time format to the local time compared to the UTC """
    local_time = datetime.utcfromtimestamp(utc_with_tz)
    return local_time.time()


city_head = Label(root, text='Enter City Name: ', font='Arial 12 bold').pack(
    pady=10)  # generate label heading

inp_city = Entry(root, textvariable=city_value, width=24, font='Arial 12 bold').pack()  # entry field

Button(root, command=showWeather, text="Check Weather: ", font="Arial 12", bg='lightblue', fg='black',
       activebackground="teal", padx=5, pady=5).pack(pady=20)

weather_now = Label(root, text="The Weather is: ", font='Arial 12 bold').pack(pady=10)

tfield = Text(root, width=46, height=10)
tfield.pack()

mainloop()  # this will initialize the application
