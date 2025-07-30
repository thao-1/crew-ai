from crewai.tools import tool

@tool("BookAppointment")
def book_appointment(date_time: str, name: str, email: str) -> str:
    """Book a 30-min slot in Google Calendar (mock)."""
    # Mock implementation (replace with real Google Calendar API in production)
    return f"✅ Slot {date_time} booked for {name} ({email})."