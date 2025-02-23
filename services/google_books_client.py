import requests
from services.config import GOOGLE_BOOKS_API_KEY, GOOGLE_BOOKS_API_URL


class GoogleBooksClient:

    def __init__(self, api_key=GOOGLE_BOOKS_API_KEY, base_url=GOOGLE_BOOKS_API_URL):
        if not api_key or not base_url:
            raise ValueError("API details are missing. Set key and url in the .env file.")

        self.api_key = api_key
        self.base_url = base_url

    def make_request(self, relative_url="", params=None):
        """Generic request function for Google Books API."""
        url = f"{self.base_url}{relative_url}"
        params = params or {}
        params["key"] = self.api_key

        try:
            response = requests.get(url, params=params)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Google Books API request failed: {str(e)}")

        return None

    def get_books(self, title, author=None, max_results=5):
        """Search for books by title, optionally filtering by author."""
        query = f"intitle:{title}"
        if author:
            query += f"+inauthor:{author}"

        params = {"q": query, "maxResults": max_results}
        data = self.make_request(params=params)
        return data.get("items", []) if data else None