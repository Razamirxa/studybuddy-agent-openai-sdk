import os
from dotenv import load_dotenv
from openai import AsyncOpenAI
from agents import Agent, Runner, OpenAIChatCompletionsModel, set_tracing_disabled

load_dotenv()

gemini_api_key = os.getenv("GEMINI_API_KEY")

client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

set_tracing_disabled(True)

studybuddy = Agent(
    name="StudyBuddy",
    instructions="""
    You are StudyBuddy, a motivational and helpful AI assistant.
    Your job is to help students organize their study routine, suggest productivity tips, and offer positive encouragement.
    Keep your tone friendly and supportive. Never offer negative feedback.
    Always end your message with a motivating question or challenge.
    """,
    model=OpenAIChatCompletionsModel(model="gemini-2.0-flash", openai_client=client)
)

def run_agent():
    result = Runner.run_sync(studybuddy, "I'm having trouble staying focused on my studies.")
    print(result.final_output)

    with open("output.md", "w") as f:
        f.write(result.final_output)
