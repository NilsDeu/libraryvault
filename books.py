class book:
    """Holding data about a book (not individual copies)."""

    def __init__(self, title: str, author: str, isbn: int) -> None:
        self.title = title
        self.author = author
        self.isbn = isbn


def add_book_from_input() -> book:
    """Create a new book from user input."""
    title = input("Please enter title: ")
    author = input("Please enter author(s): ")
    isbn = input("Please enter ISBN: ")
    return book(title, author, isbn)
