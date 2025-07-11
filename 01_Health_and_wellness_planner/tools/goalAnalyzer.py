from typing_extensions import TypedDict
from agents import function_tool, RunContextWrapper
from pydantic import BaseModel, Field, field_validator
from my_context.context import UserSessionContext

class GoalInput(BaseModel):
    quantity: float = Field(..., gt=0, description="Number of units to change (e.g. 5)")
    metric: str = Field(..., description="Measurement unit (e.g. kg, lbs)")
    duration: str = Field(..., description="Duration (e.g. '3 months')")

    @field_validator("metric")
    def metric_lower(cls, v):
        return v.lower().strip()

class GoalAnalyzerOut(TypedDict):
    parsed_goal: dict

@function_tool
async def goal_analyzer(
    ctx: RunContextWrapper[UserSessionContext],
    input: GoalInput,
) -> GoalAnalyzerOut:
    """
    Parse and validate a user's fitness goal (e.g. 'lose 5 kg in 3 months'),
    save it in the user session context, and return as JSON.
    """
    goal_dict = input.model_dump()
    ctx.context.goal = goal_dict  
    return {"parsed_goal": goal_dict}