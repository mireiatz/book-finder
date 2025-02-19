from book_fetcher import get_book_description


def main():
    print("Book Summarizer")

    title = input("Enter book title: ").strip()
    while not title:
        title = input("The title is required. Enter book title: ").strip()

    author = input("Enter author (optional): ").strip() or None

    description = get_book_description(title, author)

    if not description or description.startswith("Error") or description == "No description available.":
        print("\nCould not fetch book description. Try again.")
        return

    print("\nOriginal Description:\n", description)


if __name__ == "__main__":
    main()
