import openai
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("OPENAI_API_KEY")


class OpenAIClient:
    """Handles communication with OpenAI's API."""

    def __init__(self, api_key=API_KEY):
        if not api_key:
            raise ValueError("API details are missing. Set key and url in the .env file.")

        self.api_key = api_key

    def make_request(self, model, messages, temperature=0.7, max_tokens=150):
        """Generic request function for OpenAI's API."""
        try:
            client = openai.OpenAI()
            response = client.chat.completions.create(
                model=model,
                messages=messages,
                temperature=temperature,
                max_tokens=max_tokens
            )
            return response.choices[0].message.content.strip()
        except Exception as e:
            print(f"Error: {str(e)}")
            return None

    def generate_summary(self, description, model="gpt-3.5-turbo", max_tokens=150):
        """Sends a book description to OpenAI's API and returns a summary."""
        messages = [
            {"role": "system", "content": "You are a helpful assistant that summarizes book descriptions."},
            {"role": "user", "content": f"Concisely summarize this book description in max 3 sentences:\n\n{description}"}
        ]
        return self.make_request(model, messages, max_tokens=max_tokens)
