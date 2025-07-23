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
    """
    This tool analyzes the user's goal—either weight loss or muscle gain—and their experience 
    level—beginner or intermediate—to generate a structured 7-day workout plan line by line. 
    It returns a day-by-day list of suggested exercises tailored to the user's needs.
    """
    print("🛠️ workout tool was called")

    goal = input.goal_type.lower()
    level = input.experience_level.lower()

    plans = {
        "muscle_gain": {
            "beginner": [
                "Push-ups and bodyweight squats",
                "Dumbbell bench press and rows",
                "Rest day",
                "Shoulder presses and planks",
                "Leg day: squats and lunges",
                "Arm day: biceps/triceps",
                "Full body light workout"
            ],
            "intermediate": [
                "Barbell squats and bench press",
                "Deadlifts and pull-ups",
                "Rest day or light cardio",
                "Incline press and dips",
                "Leg press and hamstring curls",
                "Arms + core circuit",
                "Stretching + mobility"
            ]
        },
        "weight_loss": {
            "beginner": [
                "Brisk walk 30 mins",
                "Bodyweight circuit (jumping jacks, squats, push-ups)",
                "Rest or yoga",
                "Light jog or cycling",
                "Core workout (planks, crunches)",
                "Full body HIIT",
                "Stretching and rest"
            ],
            "intermediate": [
                "HIIT 20 mins + core",
                "Cardio intervals (running/cycling)",
                "Upper body strength",
                "Rest or yoga",
                "Lower body + core",
                "Full body circuit",
                "Stretch + walk"
            ]
        }
    }

    selected_plan = plans.get(goal, {}).get(level, ["Custom plan for the week."])

    final_plan = [f"Day {i+1}: {activity}" for i, activity in enumerate(selected_plan)]

    return {"weekly_workout_plan": final_plan}
