from book_fetcher import get_book_description
from summarizer import summarize_text


def main():
    print("Book Summarizer")

    # Get the title and author from user input
    title = input("Enter book title: ").strip()
    while not title:
        title = input("The title is required. Enter book title: ").strip()

    author = input("Enter author (optional): ").strip() or None

    # Get the book description
    description = get_book_description(title, author)
    if not description:
        print("Could not fetch book description")
        return

    # Summarise the description
    summary = summarize_text(description)
    if not summary:
        print("Could not summarize book description")
        return

    print("AI-Generated Summary:\n", summary)


if __name__ == "__main__":
    main()
