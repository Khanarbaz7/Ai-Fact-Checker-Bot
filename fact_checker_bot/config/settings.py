import os
from dotenv import load_dotenv

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
SERPAPI_KEY = os.getenv("SERPAPI_KEY")

DEFAULT_MODEL = "gemini-2.5-flash"
DEFAULT_TEMPERATURE = 0
MAX_TOKENS = 1024
