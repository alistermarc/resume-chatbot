import os
from dotenv import load_dotenv

load_dotenv(override=True)

PUSHOVER_TOKEN = os.getenv("PUSHOVER_TOKEN")
PUSHOVER_USER = os.getenv("PUSHOVER_USER")
GROQ_API_KEY = os.getenv("GROQ_API_KEY")