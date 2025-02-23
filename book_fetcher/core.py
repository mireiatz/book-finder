from services.google_books_client import GoogleBooksClient

client = GoogleBooksClient()


def select_book(books):
    """If multiple books are found, let the user select one and return the book ID."""
    if not books or len(books) == 0:
        return None

    # If only one book is found, confirm with the user
    if len(books) == 1:
        info = books[0]["volumeInfo"]
        print(f"\nFound: {info.get('title', 'Unknown Title')} by {', '.join(info.get('authors', ['Unknown Author']))}")
        confirm = input("Is this the book you are searching for? (y/n): ").strip().lower()
        return books[0]["id"] if confirm == "y" else None

    # If multiple books are found, let the user pick one
    print("\nPlease select the book you are searching for:")
    for i, book in enumerate(books):
        info = book["volumeInfo"]
        print(f"{i + 1}. {info.get('title', 'Unknown Title')} by {', '.join(info.get('authors', ['Unknown Author']))}")

    try:
        choice = -1
        while not 0 <= choice < len(books):
            choice = int(input("\nEnter the number to select a book: ")) - 1

        return books[choice]["id"]
    except ValueError:
        return None


def get_book_description(title, author=None):
    """Fetch the book description after confirming the correct book."""
    books = client.get_books(title, author)
    if books is None or len(books) == 0:
        return None

    book_id = select_book(books)
    if book_id is None:
        return None

    selected_book = next((book for book in books if book["id"] == book_id), None)
    if selected_book is None:
        return None

    return selected_book["volumeInfo"].get("description", None)

