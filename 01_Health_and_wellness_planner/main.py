import streamlit as st
import asyncio
import re
from datetime import date
from pydantic import BaseModel, ValidationError
from openai.types.responses import ResponseTextDeltaEvent

from agents import Agent, Runner, set_tracing_disabled
from tools.goalAnalyzer import goal_analyzer
from tools.meal_planner import meal_planner
from tools.scheduler import smart_checkin_scheduler
from tools.tracker import progress_tracker
from tools.workout_recommender import workout_recommender
from usefull_agents.injury_agent import injury_support_agent
from usefull_agents.nutrition_expert_agent import nutrition_agent
from usefull_agents.escalation_agnt import escalation_agent
from my_context.context import UserSessionContext

st.set_page_config(page_title="Health & Wellness Planner Agent", layout="centered")
st.title("🏥 Health & Wellness Planner Agent")

set_tracing_disabled(disabled=True)

main_agent = Agent[UserSessionContext](
    name="my_agent",
    instructions="""
    You are a health and wellness planning assistant. Use the following tools when relevant:
    - Use `goal_analyzer` to structure fitness goals.
    - Use `meal_planner` for 7-day dietary plans.
    - Use `workout_recommender` for workouts.
    - Use `smart_checkin_scheduler` to plan check-ins.
    - Use `progress_tracker` to log progress.
    If the user's query is unrelated or needs human support, use `handoff()` to the proper agent.
    """,
    model="gpt-3.5-turbo-1106",
    tools=[goal_analyzer, meal_planner, workout_recommender, smart_checkin_scheduler, progress_tracker],
    handoffs=[escalation_agent, injury_support_agent, nutrition_agent],
)

st.markdown("---")
st.subheader("🎯 Goal Analyzer (Optional Step)")

user_goal = st.text_area("Describe your health goal", placeholder="e.g., I want to lose 5 kg in 2 months.")

class GoalOutput(BaseModel):
    type: str
    target: str
    duration: str
    start_date: str

class GoalAnalyzerTool:
    def __init__(self):
        self.today = date.today().isoformat()

    def analyze_goal(self, user_input: str):
        if not user_input or len(user_input.strip()) < 5:
            return {"error": "Goal is too short or empty."}
        try:
            goal_type = "weight_loss" if "lose" in user_input.lower() else "muscle_gain"
            target_match = re.search(r"\d+\s?(kg|kgs|pounds|lbs|inch|inches)", user_input.lower())
            duration_match = re.search(r"\d+\s?(day|days|week|weeks|month|months)", user_input.lower())

            structured_goal = {
                "type": goal_type,
                "target": target_match.group() if target_match else "unknown",
                "duration": duration_match.group() if duration_match else "unknown",
                "start_date": self.today,
            }
            return GoalOutput(**structured_goal).model_dump()
        except ValidationError as ve:
            return {"error": "Invalid output structure", "details": str(ve)}
        except Exception as e:
            return {"error": "Something went wrong", "details": str(e)}

if st.button("🧠 Analyze Goal"):
    analyzer = GoalAnalyzerTool()
    result = analyzer.analyze_goal(user_goal)
    if "error" in result:
        st.error(result["error"])
    else:
        st.success("Structured Goal Created")
        st.json(result)

st.markdown("---")
st.subheader("💬 Chat With Your Wellness Assistant")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

chat_input = st.chat_input("Say something to your assistant...")

async def stream_chat(message: str):

    st.session_state.chat_history.append(("user", message))
    with st.chat_message("user"):
        st.write(message)

    with st.chat_message("assistant"):
        output_box = st.empty()
        streamed_response = ""
        try:
            result = Runner.run_streamed(main_agent, input=message)
            async for event in result.stream_events():
                if event.type == "raw_response_event" and isinstance(event.data, ResponseTextDeltaEvent):
                     delta = event.data.delta
                     streamed_response += delta
                     output_box.markdown(streamed_response)
            st.session_state.chat_history.append(("assistant", streamed_response))
        except Exception as e:
            error = f"❌ Error: {str(e)}"
            output_box.error(error)
            st.session_state.chat_history.append(("assistant", error))

if chat_input:
    asyncio.run(stream_chat(chat_input))

for role, msg in st.session_state.chat_history:
    st.chat_message(role).write(msg)

st.markdown("---")
st.subheader("⚡ Quick Prompts")

quick_prompts = [
    "I want to build muscle. I'm a beginner. Can you make me a 7-day workout plan?",
    "Can you make a vegetarian meal plan for the next 7 days?",
    "Can you schedule my check-in for next week?",
    "Update: I lost 1.5 kg since last week.",
]

for prompt in quick_prompts:
    if st.button(prompt):
        asyncio.run(stream_chat(prompt))

st.markdown("---")
st.markdown("🧘‍♀️ *Built with ❤️ to help you stay healthy and focused.*")
