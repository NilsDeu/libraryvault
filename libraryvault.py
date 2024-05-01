from user import librarian
import books as b


def show_main_menue(user: librarian) -> str:
    """Prints the main menue for the user."""

    print("*" * 10)
    print("LibraryManager")
    print(f"Welcome {current_user}")
    if current_user != default_user:
        print("[L]ogout")
    else:
        print("[L]ogin")

    print("[A]dd book")
    print("[D]elete book")

    print ("L[i]st books")
    print("[C]eck out book")
    print("[R]eturn book")

    print("[U]ser management")
    print("[Q]uit")

def add_librarian(first_name: str = "", last_name: str = "") -> librarian:
    """Creates a new librerian from user input."""
    if not first_name:
        first_name = input("Enter first name of librarian: ")
    if not last_name:
        last_name = input("Enter last name of librarian: ")
    return librarian(first_name, last_name)

def list_all_books(book_catalogue: list[b.book]) -> None:
    for book in book_catalogue:
        print(book)

def login() -> librarian:
    """Login w/ username and passwort."""
    name = input("enter user name: ")
    # passwort = input("enter passwort: ")
    # @todo passwort check
    # @todo load user data
    return add_librarian("", name)

def logout(current_user: librarian, default_user: librarian) -> librarian:
    """Logs out current user by setting it to guest user."""
    current_user = default_user
    return current_user


book_catalogue = []

if __name__ == "__main__":
    run_program = True
    default_user = add_librarian("guest", "user")
    current_user = default_user

    while run_program:
        show_main_menue(current_user)
        command = input("Your Choice: ").upper()
        if len(command) > 1:
            print("Commands consist of single letters only.")
        match command:
            case "A":
                book_catalogue = b.add_book(book_catalogue)
            case "C":
                print("not implemented")
            case "D":
                print("not implemented")
            case "I":
                if len(book_catalogue) > 1:
                    list_all_books(book_catalogue)
                else:
                    print("No books yet.")
            case "L":
                if current_user == default_user:  # @fix w/ userrole
                    current_user = login()
                else:
                    current_user = logout()
            case "Q":
                run_program = False
            case "R":
                print("not implemented")
            case "U":
                current_user = add_librarian()
            case _:
                print("Wrong key.")