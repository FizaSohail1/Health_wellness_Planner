from agents import function_tool
from pydantic import BaseModel, Field
from typing_extensions import TypedDict
from datetime import datetime

class ProgressUpdateInput(BaseModel):
    update: str = Field(..., description="User's progress update text")

class ProgressTrackerOut(TypedDict):
    message: str


@function_tool
async def progress_tracker(input: ProgressUpdateInput) -> ProgressTrackerOut:
    """
    Accepts user progress updates and returns a confirmation message.
    """
    print("📈 progress_tracker tool was called")  # Debug print

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")

    return {
        "message": f"✅ Progress noted on {timestamp}. Keep it up!"
    }
