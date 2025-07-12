# 🏥 Health & Wellness Planner Agent

**Health & Wellness Planner Agent** is an intelligent assistant designed to help users plan their health journey by analyzing goals, recommending workouts, generating meal plans, scheduling smart check-ins, and tracking fitness progress — all powered by tool-augmented LLM agents and contextual memory.

This project integrates **OpenAI GPT models**, custom tools, handoff, and multi-agent logic to deliver real-time, structured, and helpful wellness support.

----------

## 🚀 Features

-   💬 **Conversational Assistant** — Chat with a friendly AI wellness assistant.
    
-   🎯 **Goal Analyzer Tool** — Converts natural language fitness goals (e.g., "lose 5kg in 2 months") into structured data.
    
-   🏋️ **Workout Recommender** — Suggests a personalized 7-day workout plan based on fitness goals and experience level.
    
-   🥗 **Meal Planner** — Provides healthy 7-day meal plans (supports vegetarian options).
    
-   🗓️ **Check-in Scheduler** — Schedules motivational reminders and follow-ups.
    
-   📈 **Progress Tracker** — Allows users to log and reflect on their progress over time.
    
-   🧠 **Guardrails & Context** — Uses `pydantic` models for validation and guards against off-topic queries.
    
-   🧑‍⚕️ **Multi-Agent Support** — Includes escalation, injury, and nutrition specialist agents using handsoff.
    

----------

## 🛠️ Tech Stack

-   ✅ **Python**
    
    
-   🧰 **Function tools (with `@function_tool`)**
    
-   🧾 **Pydantic Validation**
    
-   🧱 **Custom Guardrails (input/output)**
    
-   📦 **Agents & Runner system (tool-augmented)**
    
-   🔁 **Streaming response via `Runner.run_streamed()`**
    
-   💻 **Streamlit UI**
    

----------
## 🧪 To Run the Agent (Step-by-Step)

Follow these instructions to set up and run the Health & Wellness Planner Agent in your terminal:

### ✅ 1. Clone the Repository

```
git clone https://github.com/FizaSohail1/Health_wellness_Planner.git
```
```
cd Health_wellness_Planner` 
```

----------

### ✅ 2. Create and Activate a Virtual Environment (optional but recommended)

**For Windows:**

bash

CopyEdit

`python -m venv venv
venv\Scripts\activate` 

**For macOS/Linux:**

bash

CopyEdit

`python3 -m venv venv source venv/bin/activate` 

----------

### ✅ 3. Install Dependencies

```
`uv add openai-agents` 
```
```
`uv add streamlit` 
```
----------

### ✅ 4. Add Your OpenAI API Key

Create a `.env` file in the root directory and add:

```
`OPENAI_API_KEY=your_openai_key_here` 
```

----------

### ✅ 5. Run the Agent
```
`streamlit run main.py` 
```
----------
## 🔒 Guardrails

All tools and agents include guardrails for input validation and restricted responses. This ensures:

-   Accurate input formats
    
-   Safe output generation

----------

## 📌 Future Updates

🔧 This is an active project. Upcoming improvements:

-   ✅ More personalized plan generation using dynamic context
    
-   🖼️ Image and chart support in the UI
    
-   📋 User authentication and session memory
----------

## Author

**Fiza Sohail**  