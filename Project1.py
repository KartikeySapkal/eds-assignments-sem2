import json
import requests
import os
x="yes"
while(True): 
    x= input("Enter y to run or q to quite: ")
    if x== 'q': 
        print(f'Bye Bye')
        break

    elif x  ==  "y":
             
        print(f"please Enter Your City Name: ")
        city = input("Enter City Name: ")
        
        print(f"telling about {city}")

        url = f'http://api.weatherapi.com/v1/current.json?key=fc30e9f0563f4b63940135810231704&q={city}'

        r= requests.get(url)
        # print(r.text)
        wdic = json.loads(r.text)
        w = wdic["current"]["temp_c"]
        condition = wdic["current"]["condition"]["text"]
        Wind_speed = wdic["current"]["wind_mph"]
        humidity = wdic["current"]["humidity"]

        print(f"The current temperature in {city} is {w}  Degree Celcius")
        print(f"And The weather condition seems to be {condition}")
        print(f"Also the wind speed is around {Wind_speed} miles per Hours")
        print(f"Humidity is around {humidity}")
        
       

        