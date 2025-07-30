# AI-Powered Appointment Scheduler with CrewAI

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

An intelligent scheduling assistant that books appointments by processing natural language input. Built with CrewAI, this system demonstrates how AI can automate calendar management through natural language understanding.

## ✨ Features

- **Natural Language Processing**: Understands appointment details from plain English
- **Mock Calendar Integration**: Simulates Google Calendar booking (can be extended to real APIs)
- **Error Handling**: Robust input validation and error management
- **Environment Management**: Secure handling of API keys and configurations
- **Modular Design**: Easy to extend with additional features and integrations

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- OpenAI API key

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/scheduler-crew.git
   cd scheduler-crew
   ```

2. **Set up a virtual environment** (recommended)
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment variables**
   Create a `.env` file in the project root:
   ```env
   OPENAI_API_KEY=your_openai_api_key_here
   ```

## 🛠️ Usage

Run the scheduler:
```bash
python main.py
```

Example input:
```
Book an appointment for John Doe on August 20th at 2:30 PM with email john.doe@example.com
```

## 🏗️ Project Structure

```
scheduler-crew/
├── .env                 # Environment variables
├── .gitignore           # Git ignore rules
├── README.md            # This file
├── main.py              # Entry point
├── agents.py            # Agent definitions
├── tasks.py             # Task definitions
└── tools.py             # Custom tools
```

## 🤖 Components

### `main.py`
The orchestrator that ties everything together:
- Loads environment variables
- Handles user input
- Creates and executes the crew

### `agents.py`
Defines the scheduling agent with its role and capabilities.

### `tasks.py`
Manages the appointment booking task with clear input/output specifications.

### `tools.py`
Contains the booking functionality (currently a mock implementation).

## 🔍 How It Works

1. The user provides appointment details in natural language
2. The CrewAI agent parses the input to extract:
   - Date and time
   - Attendee name
   - Email address
3. The booking tool processes the request
4. A confirmation message is returned

## 🛠️ Extending the Project

### Connecting to Real Calendar APIs
Replace the mock implementation in `tools.py` with actual API calls to:
- Google Calendar
- Microsoft Outlook
- Calendly
- etc.

### Adding Features
- Recurring appointments
- Meeting room booking
- Calendar conflict detection
- Email notifications
- Web interface

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [CrewAI](https://www.crewai.com/) for the agent framework
- [OpenAI](https://openai.com/) for the language models
- [python-dotenv](https://github.com/theskumar/python-dotenv) for environment management

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
