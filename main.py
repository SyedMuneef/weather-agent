from ai_agents import Weather_Agent
from agents import Runner
import chainlit as cl

# Initialize the weather agent
Weather_Agent = Weather_Agent

@cl.on_chat_start
async def handle_chat_start():
    await cl.Message(content="Hello! I will provide you with weather information.").send()

@cl.on_message
async def handle_message():
    # Convert the Chainlit chat context to OpenAI format
    chat_history = cl.chat_context.to_openai()

    try:
        # Run without streaming to avoid validation error from Gemini
        result = await Runner.run(Weather_Agent, chat_history)

        # Send the full response
        await cl.Message(content=result.response).send()

    except Exception as e:
        # Catch and log any issues
        await cl.Message(content="⚠️ Something went wrong: " + str(e)).send()
        print("Error during agent execution:", e)
