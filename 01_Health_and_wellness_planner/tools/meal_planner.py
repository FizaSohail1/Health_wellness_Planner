from typing import List
from agents import function_tool
from pydantic import BaseModel, Field
from typing_extensions import TypedDict

# 🟩 Input model
class MealPlanInput(BaseModel):
    dietary_preference: str = Field(..., description="User's dietary preference, e.g., vegetarian, keto, high-protein")

# 🟩 Output structure
class MealPlannerOut(TypedDict):
    weekly_meal_plan: List[List[str]]  # Each day has a list of 3 meals

# 🛠️ Tool
@function_tool
async def meal_planner(input: MealPlanInput) -> MealPlannerOut:
    """
    Suggest a simple 7-day meal plan based on the user's dietary preference.
    """

    print("🍽️ meal_planner tool called")  # 🪵 Debug line

    sample_meal = f"{input.dietary_preference.title()} Meal"

    weekly_meal_plan = [
        [f"{sample_meal} - Breakfast", f"{sample_meal} - Lunch", f"{sample_meal} - Dinner"]
        for _ in range(7)
    ]

    return {"weekly_meal_plan": weekly_meal_plan}
