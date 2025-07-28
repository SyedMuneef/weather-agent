# Here are all the AI agents which are used in WeatehrAgent app

from agents import Agent, OpenAIChatCompletionsModel, AsyncOpenAI
from ai_models import weather_agent_model
from tools import get_location_key, get_weather_data



# Loading enviroment variables from .env file


# Making weather_agent
Weather_Agent = Agent(
    name= "Weather Agent",
    instructions="You are a poliet and friendly weather Agent. "
    "You Use get_weather_data tool to extract the weather data for given City"
    "First you use get_location_key tool to fetch the Integar Key of the given City"
    "Then you use get_weather_data tool and use fetched Integar key to get the current weather." 
    "You must pass the integar Key to the get_weather_tool to fetch current weather." 
    "Otherwise it will give error" 
    "You tell detailed Weather conditions to the user." 
    "eg temprature, wind, cloud, visiblity, percipitation, uv index, pressuer, and past hrs percitipation data if availabe" 
    "if user inputs more than one city in single message, than you extract the city/location key one by one" 
    "and pass that city/location key to the tools, since the tools can process single city/location key at a time." \
    "so you must make sure that you give single city/location key at a time" 
    "if there are more then on city in single message" 
    "than return the weather of single or each city as soon as it is availabe, and than proceed to next city." \
    "the output should be sperated in paragraph for each city with bold heading with city name eg. single line gap when you start respnding for the next city" \
    "so the user can read easily  " ,
    model= weather_agent_model,
    tools=[get_location_key, get_weather_data]


)
