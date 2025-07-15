from typing_extensions import TypedDict
from agents import function_tool, RunContextWrapper
from pydantic import BaseModel
from my_context.context import UserSessionContext
import re

class GoalAnalyzerOut(TypedDict):
    parsed_goal: dict

class StructuredGoal(BaseModel):
    type: str
    target: str
    duration: str

@function_tool
async def goal_analyzer(
    ctx: RunContextWrapper[UserSessionContext],
    input: str,
) -> GoalAnalyzerOut:
    """
    Extracts and parses the fitness goal from user prompt (e.g. 'I want to lose 5 kg in 3 months'),
    saves it into session context, and returns it as structured goal.
    """

    print("Goal analyzer tool called")

    goal_type = "weight_loss" if "lose" in input.lower() else "muscle_gain"
    target_match = re.search(r"\d+\s?(kg|kgs|pounds|lbs|inch|inches)", input.lower())
    duration_match = re.search(r"\d+\s?(day|days|week|weeks|month|months)", input.lower())

    goal_data = {
        "type": goal_type,
        "target": target_match.group() if target_match else "unknown",
        "duration": duration_match.group() if duration_match else "unknown",
    }

    try:
        structured = StructuredGoal(**goal_data)
        ctx.context.goal = structured.model_dump()

        print("✅ Saved Goal Context:", ctx.context.goal)

        return {"parsed_goal": structured.model_dump()}

    except Exception as e:
        print("Goal parsing failed:", str(e))
