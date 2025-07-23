from typing import List
from agents import function_tool
from pydantic import BaseModel, Field
from typing_extensions import TypedDict

class MealPlanInput(BaseModel):
    dietary_preference: str = Field(..., description="User's dietary preference, e.g., vegetarian, keto, high-protein")

class MealPlannerOut(TypedDict):
    weekly_meal_plan: List[List[str]]

@function_tool
async def meal_planner(input: MealPlanInput) -> MealPlannerOut:
    """
    Use this tool to generate a weekly meal plan for the user based on their dietary preference.
    It supports vegetarian and keto options. If the preference is not recognized, it defaults to vegetarian.

    Example user inputs to trigger this tool:
    - "Can you make a vegetarian meal plan for me?"
    - "I want a weekly keto diet plan"
    - "Give me high-protein meals" (if later extended)

    Input: dietary_preference (e.g., vegetarian, keto)
    Output: weekly_meal_plan (list of 7 days with 3 meals each)
    """

    meal_options = {
        "vegetarian": [
            ["Oatmeal with fruits", "Veggie stir fry with tofu", "Lentil curry with rice"],
            ["Greek yogurt with granola", "Chickpea salad", "Stuffed bell peppers"],
            ["Smoothie bowl", "Grilled cheese & tomato soup", "Paneer tikka with roti"],
            ["Avocado toast", "Vegetable pasta", "Spinach & mushroom curry"],
            ["Poha", "Veggie wrap", "Rajma chawal"],
            ["Banana pancakes", "Mixed bean salad", "Vegetable biryani"],
            ["Paratha with curd", "Minestrone soup", "Chole bhature"],
        ],
        "keto": [
            ["Scrambled eggs", "Grilled chicken salad", "Zucchini noodles with pesto"],
            ["Chia seed pudding", "Avocado chicken bowl", "Cauliflower crust pizza"],
            ["Cheese omelette", "Tuna salad", "Beef stir fry"],
            ["Bulletproof coffee", "Egg salad lettuce wraps", "Salmon and asparagus"],
            ["Almond pancakes", "Broccoli cheddar soup", "Grilled shrimp with veggies"],
            ["Boiled eggs", "Zoodles with meatballs", "Keto butter chicken"],
            ["Yogurt with flaxseeds", "Cobb salad", "Steak and roasted cauliflower"],
        ],
    }

    preference = input.dietary_preference.lower()
    weekly_meal_plan = meal_options.get(preference)

    if not weekly_meal_plan:
        weekly_meal_plan = meal_options["vegetarian"]

    return {"weekly_meal_plan": weekly_meal_plan}
