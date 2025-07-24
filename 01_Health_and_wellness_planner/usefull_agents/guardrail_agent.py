from pydantic import BaseModel, Field
from agents import Agent
from dotenv import load_dotenv

load_dotenv()

class HealthWellnessOutput(BaseModel):
    is_unrelated_query: bool = Field(description="Set true if there is something unrelated to health wellness")
    res: str


guardrail_agent = Agent(
     name="escalation-agent",
    instructions="""
     You will check if the user query is related to health or wellness 
    """,
    model="gpt-4.1-mini",
    output_type= HealthWellnessOutput
)