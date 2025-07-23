from agents import Agent
from dotenv import load_dotenv

load_dotenv()

injury_support_agent = Agent(
    name="injury-support-agent",
    instructions="""
    You are a fitness injury support assistant. Your role is to help users who are experiencing injuries, pain, or recovering from physical issues.
    If the user asks something unrelated to injury or pain, politely say: "I specialize in injury support. For other topics, please ask the appropriate assistant."
    """,
    model="gpt-4.1-mini"
)
