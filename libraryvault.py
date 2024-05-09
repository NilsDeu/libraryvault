from gettext import translation as l10n, gettext as _

from user import librarian
import books as b


def show_main_menue(user: librarian, vault_name: str) -> str:
    """Prints the main menue for the user."""

    print("*" * 10)
    print(vault_name)
    print(_("Welcome, {user}").format(user=current_user))
    print("*" * 10)
    if current_user != default_user:
        print(_("[L]ogout"))
    else:
        print(_("[L]ogin"))

    print(_("[A]dd book"))
    print(_("[D]elete book"))

    print(_("L[i]st books"))
    print(_("[C]eck out book"))
    print(_("[R]eturn book"))

    print(_("[U]ser management"))
    print(_("[Q]uit"))


def add_librarian(first_name: str = "", last_name: str = "") -> librarian:
    """Creates a new librerian from user input."""
    if not first_name:
        first_name = input(_("Enter first name of librarian: "))
    if not last_name:
        last_name = input(_("Enter last name of librarian: "))
    return librarian(first_name, last_name)


def list_all_books(book_catalogue: list[b.book]) -> None:
    for book in book_catalogue:
        print(book)


def login() -> librarian:
    """Login w/ username and passwort."""
    name = input(_("enter user name: "))
    # passwort = input(_("enter passwort: "))
    # @todo passwort check
    # @todo load user data
    return add_librarian("", name)


def logout(current_user: librarian, default_user: librarian) -> librarian:
    """Logs out current user by setting it to guest user."""
    current_user = default_user
    return current_user


vault_name = "libraryVault"
localedir = "./locales"
domain = localedir + "/" + vault_name
system_language = l10n(domain, localedir, fallback=True, languages=["en"])

book_catalogue = []

if __name__ == "__main__":
    run_program = True
    default_user = add_librarian("guest", "user")
    current_user = default_user

    while run_program:
        show_main_menue(current_user, vault_name)
        command = input(_("Your Choice: ")).upper()
        if len(command) > 1:
            print(_("Commands consist of single letters only."))
        match command:
            case "A":
                book_catalogue = b.add_book(book_catalogue)
            case "C":
                print(_("not implemented"))
            case "D":
                print(_("not implemented"))
            case "I":
                if len(book_catalogue) > 1:
                    list_all_books(book_catalogue)
                else:
                    print(_("No books yet."))
            case "L":
                if current_user == default_user:  # @fix w/ userrole
                    current_user = login()
                else:
                    current_user = logout()
            case "Q":
                run_program = False
            case "R":
                print(_("not implemented"))
            case "U":
                current_user = add_librarian()
            case _:
                print(_("Wrong key."))
