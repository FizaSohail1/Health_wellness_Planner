from agents import Agent, set_tracing_disabled
from dotenv import load_dotenv

load_dotenv()
set_tracing_disabled(disabled=True)


escalation_agent = Agent(
    name="escalation-agent",
    instructions="""
    You are an escalation assistant. Your role is to detect when a user wants to speak with a human coach or needs human help.
    If the user asks about anything else do not respond or give any answers e.g., "I'm only here to escalate you."
    Just ignore it silently — your job is only to escalate, not to assist or explain. Always show this ✅ emoji before the response.
    """,
    model="gpt-4.1-mini",
)
