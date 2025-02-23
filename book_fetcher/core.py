from services.google_books_client import GoogleBooksClient

client = GoogleBooksClient()


def filter_books_by_exact_match(books, title, author=None):
    """Filter books to find an exact title match, and optionally match author."""
    for book in books:
        volume_info = book.get("volumeInfo", {})
        exact_title_match = volume_info.get("title", "").strip().lower() == title.strip().lower()

        if exact_title_match:
            if author:
                authors = [a.lower() for a in volume_info.get("authors", [])]
                if author.lower() in authors:
                    return [book]
            else:
                return [book]

    return books


def select_book(books):
    """If multiple books are found, let the user select one and return the book ID."""
    if not books or len(books) == 0:
        return None

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
    if not books:
        return None

    books = filter_books_by_exact_match(books, title, author)

    # If only one book is found/matched, confirm with the user
    if len(books) == 1:
        info = books[0]["volumeInfo"]
        print(f"\nFound: {info.get('title', 'Unknown Title')} by {', '.join(info.get('authors', ['Unknown Author']))}")
        confirm = input("Is this the book you are searching for? (y/n): ").strip().lower()
        if confirm == "y":
            return books[0]["volumeInfo"].get("description", None)

    book_id = select_book(books)
    if book_id is None:
        return None

    selected_book = next((book for book in books if book["id"] == book_id), None)
    return selected_book["volumeInfo"].get("description", None) if selected_book else None


