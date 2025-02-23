import os
from dotenv import load_dotenv

load_dotenv()

GOOGLE_BOOKS_API_KEY = os.getenv("GOOGLE_BOOKS_API_KEY")
GOOGLE_BOOKS_API_URL = os.getenv("GOOGLE_BOOKS_API_URL")

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
