from google_books_client import GoogleBooksClient

client = GoogleBooksClient()


def fetch_books(title, author=None):
    """Fetch books by title (and optionally author) and return a list of matching books."""
    return client.get_books_by_author_and_title(title, author) if author else client.get_books_by_title(title)


def select_book(books):
    """If multiple books are found, let the user select one and return the book ID."""
    if not books:
        return None

    # If only one book is found, confirm with the user
    if len(books) == 1:
        book_info = books[0]["volumeInfo"]
        print(
            f"\nFound: {book_info.get('title', 'Unknown Title')} by {', '.join(book_info.get('authors', ['Unknown Author']))}")
        confirm = input("Is this the correct book? (y/n): ").strip().lower()
        return books[0]["id"] if confirm == "y" else None

    # If multiple books are found, let the user pick one
    print("\nMultiple books found. Please select the correct one:")
    for i, book in enumerate(books):
        info = book["volumeInfo"]
        print(f"{i + 1}. {info.get('title', 'Unknown Title')} by {', '.join(info.get('authors', ['Unknown Author']))}")

    try:
        choice = -1
        while not 0 <= choice < len(books):
            choice = int(input("\nEnter the number to select a book: ")) - 1

        return books[choice]["id"]
    except ValueError:
        return books[0]["id"]


def get_book_description(title, author=None):
    """Fetch the book description after confirming the correct book."""
    books = fetch_books(title, author)

    if not books:
        return "No books found."

    book_id = select_book(books)

    if not book_id:
        return "Could not confirm a valid book."

    book = client.get_book_by_id(book_id)
    return book["volumeInfo"].get("description", "No description available.")
