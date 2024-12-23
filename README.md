# AI Cryptocurrency Chatbox

## Decription: 

This is a Flask-based AI chatbox powered by a fine-tuned OpenAI model, designed to answer cryptocurrency-related queries. The app provides a user-friendly web interface for real-time interactions and is deployed using Render.

## Features:

- Real-time chat interface for cryptocurrency queries.
- Powered by a fine-tuned OpenAI GPT model.
- Deployed for public access with a secure backend.


## Technical Used:

- Flask (Backend Framework)
- OpenAI API (AI Model Integration)
- HTML, CSS, JavaScript (Frontend)
- Gunicorn (Production Server)
- Render (Deployment Platform)

## SetUp and Installation:

1. Clone the repository
2. Navigate to the project directory
3. Create a virtual environment and activate it:
   python -m venv venv
   source venv/bin/activate  or on Windows: venv\Scripts\activate
4. Install dependencies:
   pip install -r requirements.txt
5. Set your OpenAI API key:
   - Create a `.env` file in the root directory.
   - Add: OPENAI_API_KEY=your_openai_api_key_here
6. Run the app locally:
   python app.py