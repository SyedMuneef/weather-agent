# Here are all the AI models which are used in Weather_Agent

from dotenv import load_dotenv
import os
from agents import  OpenAIChatCompletionsModel, AsyncOpenAI

load_dotenv()

# Defining Model provider
provider = AsyncOpenAI(
    api_key = os.getenv("GEMINI_API_KEY"),
    base_url= "https://generativelanguage.googleapis.com/v1beta/openai/"
    
)

# Defining Model
weather_agent_model = OpenAIChatCompletionsModel(
    model= "gemini-2.5-flash-lite-preview-06-17",
    openai_client= provider

)