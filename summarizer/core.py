from services.openai_client import OpenAIClient

client = OpenAIClient()


def summarize_text(description):
    """Fetches the AI-generated summary using OpenAIClient."""
    return client.generate_summary(description, None)
