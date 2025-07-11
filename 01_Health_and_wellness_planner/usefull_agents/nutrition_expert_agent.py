from agents import Agent, set_tracing_disabled
from dotenv import load_dotenv
from openai.types.responses import ResponseTextDeltaEvent
from my_context.context import UserSessionContext
from tools.meal_planner import meal_planner

load_dotenv()
set_tracing_disabled(disabled=True)


nutrition_agent = Agent(
    name= "nutrition-agent",
    instructions="You are a nutrition expert. Your job is to guide the user with meal planning and nutritional advice based on their fitness goals. If user asks something unrelated to food or nutrition just politely say: “I am here to help with nutrition and diet. For other topics, please ask the appropriate assistant. always shown this 🍕 emoji before the response",
    model= "gpt-3.5-turbo-1106",
    # context_type=UserSessionContext,
    tools=[meal_planner]
)
