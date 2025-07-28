# Here are all the tools which used by Weather_Agent Agent in Weather Agent app

import requests as rq
from dotenv import load_dotenv
from agents import function_tool
import os

# Loading of Env File
load_dotenv()

# This tool fetch Key of the given city. The key will be passed to get_weather_data tool
#  to fetch current weather of the city
@function_tool
def get_location_key(location: str):
   """
   This tool uses Accu Location API to get The Key of the City.
   The args of location takes the String Value eg. name of the city returns the Key an integar value. 
   This Key is then Used as input for get_weather_data tool to fatch the current condtion of weather
   for given city
   Remeber, the tool takes single arguent at a time and returns single location.
   dont pass more than one argument or it will throw error
    """
   try:
    res = rq.get(f"http://dataservice.accuweather.com/locations/v1/search?apikey={os.getenv("ACCU_WEATHER_API_KEY")}&q={location}&details=false")
    data = res.json()
    return data[0]['Key'] 
   except:
    return(f"{res.status_code}:")


# This tool will use City key to fetch weather
@function_tool
def get_weather_data(location: int):
   """This tool uses Accue Weather API to get Current Weather Information.
    the location arg takes the integare value of location which is fecth using get_location_key tool
    and returns detailed weather data. 
   Remeber, the tool takes single argument at a time and returns single city, weather.
   dont pass more than one argument or it will throw error
   """
   try:
    res = rq.get(f"http://dataservice.accuweather.com/currentconditions/v1/{location}?apikey={os.getenv("ACCU_WEATHER_API_KEY")}&details=true")
    data = res.json()
    return data
   except:
    return f"{res.status_code}:"

