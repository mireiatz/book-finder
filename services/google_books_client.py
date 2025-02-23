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

        response = requests.get(url, params=params)
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"Google Books API Error: {response.status_code}")

    def get_books_by_title(self, title, max_results=5):
        """Search for books by title"""
        params = {"q": f"intitle:{title}", "maxResults": max_results}
        data = self.make_request(params=params)
        return data.get("items", [])

    def get_books_by_author_and_title(self, title, author, max_results=5):
        """Search for books by title and author"""
        params = {"q": f"intitle:{title}+inauthor:{author}", "maxResults": max_results}
        data = self.make_request(params=params)
        books = data.get("items", [])

        if not books:
            return []

        # Exact match filtering
        for book in books:
            volume_info = book.get("volumeInfo", {})
            if volume_info.get("title", "").strip().lower() == title.strip().lower() and \
                    author.lower() in [a.lower() for a in volume_info.get("authors", [])]:
                return [book]  # Return the exact match as a single-item list

        # If no exact match is found, return all fuzzy results
        return books

    def get_book_by_id(self, book_id):
        """Retrieve a specific book by ID."""
        return self.make_request(relative_url=f"/{book_id}")
