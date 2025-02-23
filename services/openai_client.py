import openai
from services.config import OPENAI_API_KEY


class OpenAIClient:

    def __init__(self, api_key=OPENAI_API_KEY):
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
            print(f"OpenAPI request failed: {str(e)}")

        return None

    def generate_summary(self, description, model="gpt-3.5-turbo", max_tokens=150):
        """Sends a description to OpenAI's API and returns a summary."""
        messages = [
            {"role": "system", "content": "You are a helpful assistant that summarizes descriptions."},
            {"role": "user", "content": f"Concisely summarize this description in max 3 sentences:\n\n{description}"}
        ]
        data = self.make_request(model, messages, max_tokens=max_tokens)
        return data if data else None
