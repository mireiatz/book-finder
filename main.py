from book_fetcher import get_book_description


def main():
    print("Book Summarizer")

    # Get the title and author from user input
    title = input("Enter book title: ").strip()
    while not title:
        title = input("The title is required. Enter book title: ").strip()

    author = input("Enter author (optional): ").strip() or None

    # Get the book description
    description = get_book_description(title, author)
    print(description)
    if not description or description.startswith("No description available") or description.startswith("No books found"):
        print("Could not fetch book description")
        return


if __name__ == "__main__":
    main()
