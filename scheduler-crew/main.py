from crewai import Crew
from agents import scheduler
from tasks import create_scheduling_task
from dotenv import load_dotenv
import os

def main():
    # Load environment variables from .env file
    load_dotenv()
    
    # Verify OpenAI API key is set
    if not os.getenv("OPENAI_API_KEY"):
        print("Error: OPENAI_API_KEY is not set in the .env file")
        print("Please add your OpenAI API key to the .env file and try again.")
        return
    
    # Example user input (in real life, this could come from a UI or CLI)
    user_input = input("Please enter appointment details (e.g., 'Book an appointment for John Doe on 2025-08-01 at 10:00 AM with email john.doe@example.com'): ")
    
    if not user_input.strip():
        print("No input provided. Using example input.")
        user_input = "Book an appointment for John Doe on 2025-08-01 at 10:00 AM with email john.doe@example.com"
    
    try:
        # Create task and crew
        task = create_scheduling_task(user_input)
        crew = Crew(
            agents=[scheduler],
            tasks=[task],
            verbose=True
        )
        
        # Run the crew
        print("\nProcessing your appointment request...\n")
        result = crew.kickoff()
        print("\n" + "="*50)
        print("APPOINTMENT SCHEDULING RESULT:")
        print("="*50)
        print(result)
        print("="*50)
        
    except Exception as e:
        print(f"\nAn error occurred: {str(e)}")
        print("Please check your input and try again.")

if __name__ == "__main__":
    main()