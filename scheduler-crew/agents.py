from crewai import Agent
from tools import book_appointment

scheduler = Agent(
    role="Appointment Scheduler",
    goal="Find a free slot and book appointments based on user input",
    backstory="You are an efficient scheduling assistant who books appointments accurately.",
    tools=[book_appointment],
    verbose=True,
    allow_delegation=False
)