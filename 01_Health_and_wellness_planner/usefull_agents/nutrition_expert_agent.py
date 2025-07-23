from agents import Agent 
from dotenv import load_dotenv
from tools.meal_planner import meal_planner

load_dotenv()

nutrition_agent = Agent(
    name= "nutrition-agent",
    instructions="You are a nutrition expert. Your job is to guide the user with meal planning and nutritional advice based on their fitness goals. If user asks something unrelated to food or nutrition just politely say: “I am here to help with nutrition and diet. For other topics, please ask the appropriate assistant.",
    model= "gpt-3.5-turbo-1106",
    tools=[meal_planner]
)
