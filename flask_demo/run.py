# run.py
from app import create_app
from dotenv import load_dotenv
import os

# Load environment variables from .env file explicitly if needed
# (Flask usually does this automatically with .flaskenv and python-dotenv installed)
# load_dotenv(os.path.join(os.path.dirname(__file__), '.env'))

app = create_app()

if __name__ == '__main__':
    # Use debug=True only in development
    # In production, use a proper WSGI server like Gunicorn or uWSGI
    app.run(debug=True) # Debug will be controlled by FLASK_ENV=development

