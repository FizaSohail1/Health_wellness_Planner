from typing_extensions import TypedDict
from datetime import datetime, timedelta
from agents import function_tool

class SmartCheckinOut(TypedDict):
    message: str
    next_checkin: str

@function_tool
async def smart_checkin_scheduler() -> SmartCheckinOut:
    """
    Schedules a check-in 7 days from today.
    No input needed. Just returns the next check-in date.
    """
    next_date = datetime.now() + timedelta(days=7)
    formatted_date = next_date.strftime("%A, %B %d, %Y")

    return {
        "message": f"✅ Your next check-in is scheduled on {formatted_date}.",
        "next_checkin": formatted_date
    }
