# This is main file of the programming, here also defined the UI of the app

from ai_agents import Weather_Agent
from agents import Runner
import chainlit as cl
import time
from openai.types.responses import ResponseTextDeltaEvent



Weather_Agent = Weather_Agent # Intializing Weather_Agent


@cl.on_chat_start
async def handle_chat_start(): # this function will handle all the actions/functionality when user opens the chat.
    await cl.Message(content="Hello I Will provide you weather Information!!!").send() # show greeting message on ui when user opens chat



@cl.on_message
async def handle_message():
    chat_history = cl.chat_context.to_openai()
    result = Runner.run_streamed(Weather_Agent, chat_history)
    reply = cl.Message(content="")
    async for event in result.stream_events():
        if event.type == "raw_response_event" and isinstance(event.data, ResponseTextDeltaEvent):
            await reply.stream_token(event.data.delta)
            
    await reply.send()

     
  
   

