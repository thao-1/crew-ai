from crewai import Task
from tools import book_appointment

def create_scheduling_task(user_input: str):
    return Task(
        description=f"Parse the user input: '{user_input}'. Extract date, time, name, and email, then book the appointment.",
        expected_output="A confirmation message with the booked slot details.",
        agent=None,  # Will be assigned in main.py
        tools=[book_appointment]
    )