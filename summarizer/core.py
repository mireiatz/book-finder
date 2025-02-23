from services.openai_client import OpenAIClient

client = OpenAIClient()


def summarize_text(description):
    """Fetches the AI-generated summary using OpenAIClient."""
    try:
        return client.generate_summary(description)
    except Exception:
        return None
