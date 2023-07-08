import json
import requests
import os
x="yes"
while(True): 
    x= input("Enter y to run or q to quite: ")
    if x== 'q': 
        os.system(f'say Bye Bye')
        break

    elif x  ==  "y":
             
        os.system(f"say please Enter Your City Name: ")
        city = input("Enter City Name: ")
        
        os.system(f"say telling about {city}")

        url = f'http://api.weatherapi.com/v1/current.json?key=fc30e9f0563f4b63940135810231704&q={city}'

        r= requests.get(url)
        # print(r.text)
        wdic = json.loads(r.text)
        w = wdic["current"]["temp_c"]
        condition = wdic["current"]["condition"]["text"]
        Wind_speed = wdic["current"]["wind_mph"]
        humidity = wdic["current"]["humidity"]

        os.system(f"say The current temperature in {city} is {w}  Degree Celcius")
        os.system(f"say And The weather condition seems to be {condition}")
        os.system(f"say Also the wind speed is around {Wind_speed} miles per Hours")
        os.system(f"say Humidity is around {humidity}")
        
       

        