import asyncio
from agents import Agent, Runner, set_tracing_disabled
from dotenv import load_dotenv
from pydantic import BaseModel, Field
from my_context.context import UserSessionContext


load_dotenv()
set_tracing_disabled(disabled=True)

# Guardrails
class InjuryInput(BaseModel):
    message: str = Field(..., description="User input related to injuries or recovery")

class InjuryOutput(BaseModel):
    response: str = Field(..., description="Response with injury advice or redirection")

# Agent
injury_support_agent = Agent(
    name="injury-support-agent",
    instructions="""
    You are a fitness injury support assistant. Your role is to help users who are experiencing injuries, pain, or recovering from physical issues.
    If the user asks something unrelated to injury or pain, politely say: "⚕️ I specialize in injury support. For other topics, please ask the appropriate assistant."
    Always show a ⚕️ emoji before the response.
    """,
    model="gpt-3.5-turbo-1106",
    input_guardrails=InjuryInput,
    output_guardrails=InjuryOutput
)
