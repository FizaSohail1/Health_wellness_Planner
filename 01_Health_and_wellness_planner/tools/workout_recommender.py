from typing import List, TypedDict
from agents import function_tool
from pydantic import BaseModel, Field


class WorkoutInput(BaseModel):
    goal_type: str = Field(..., description="e.g., 'weight_loss' or 'muscle_gain'")
    experience_level: str = Field(..., description="e.g., 'beginner', 'intermediate', 'advanced'")

class WorkoutPlanOut(TypedDict):
    weekly_workout_plan: List[str]

@function_tool
async def workout_recommender(input: WorkoutInput) -> WorkoutPlanOut:
    print("🛠️ workout tool was called")
    """
    Returns a dummy 7-day workout plan based on user goal and experience level.
    The agent will replace this later with specific workout steps.
    """
    dummy_plan = [f"Day {i+1}: Placeholder workout for {input.goal_type} ({input.experience_level})" for i in range(7)]
    
    return {"weekly_workout_plan": dummy_plan}
