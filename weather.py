from datetime import datetime
import os
import pytz
import requests
import math
API_KEY = 'b8bd5e0e73c6c3d812de0a7db9480964' 
API_URL = ('http://api.openweathermap.org/data/2.5/weather?q={}&mode=json&units=metric&appid={}')


def query_api(city): 
    try: 
        print(API_URL.format(city, API_KEY))        
        data = requests.get(API_URL.format(city, API_KEY)).json() 
    except Exception as exc: 
        print(exc)       
        data = None 
    return data
