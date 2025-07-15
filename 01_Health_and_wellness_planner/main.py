import streamlit as st
import asyncio
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


st.set_page_config(page_title="Wellness Chat", layout="centered")
st.title("🏥 Health & Wellness Planner Assistant")

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
    If the user's query is unrelated or needs human support, use the given agents to give the proper response.
    """,
    model="gpt-3.5-turbo-1106",
    tools=[
        goal_analyzer,
        meal_planner,
        workout_recommender,
        smart_checkin_scheduler,
        progress_tracker,
    ],
    handoffs=[
        escalation_agent,
        injury_support_agent,
        nutrition_agent,
    ],
)


if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

st.markdown("---")
st.subheader("💬 Chat With Your Wellness Assistant")

chat_input = st.chat_input("Say something to your assistant...")

async def run_agent_chat(message: str):
    context = UserSessionContext()
    st.session_state.chat_history.append(("user", message))
    
    with st.chat_message("user"):
        st.write(message)

    with st.chat_message("assistant"):
        output_box = st.empty()
        streamed_response = ""
        try:
            result = Runner.run_streamed(main_agent, input=message, context=context)
            async for event in result.stream_events():
                if event.type == "raw_response_event" and isinstance(event.data, ResponseTextDeltaEvent):
                    delta = event.data.delta or ""
                    streamed_response += delta
                    output_box.markdown(streamed_response)
            st.session_state.chat_history.append(("assistant", streamed_response))
        except Exception as e:
            error = f"❌ Error: {str(e)}"
            output_box.error(error)
            st.session_state.chat_history.append(("assistant", error))


if chat_input:
    asyncio.run(run_agent_chat(chat_input))

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
        asyncio.run(run_agent_chat(prompt))

st.markdown("---")
st.markdown("📖 *Built with ❤️ to help you learn and grow.*")
