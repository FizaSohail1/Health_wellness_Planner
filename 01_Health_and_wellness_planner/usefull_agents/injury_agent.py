import asyncio
from agents import Agent, Runner, set_tracing_disabled
from dotenv import load_dotenv
from my_context.context import UserSessionContext

load_dotenv()
set_tracing_disabled(disabled=True)


injury_support_agent = Agent(
    name= "injury-support-agent",
    instructions="You are a fitness injury support assistant. Your role is to help users who are experiencing injuries, pain, or recovering from physical issues. If the user asks something unrelated to injury or pain, politely say:I specialize in injury support. For other topics, please ask the appropriate assistant. always shown this  emoji before the response",
    model= "gpt-3.5-turbo-1106",
    # context_type=UserSessionContext,
)

