from user import librarian


def show_main_menue(user: librarian) -> str:
    """Prints the main menue for the user."""

    print("*" * 10)
    print("LibraryManager")
    if user.first_name != "guest" and user.last_name != "user":
        # @fix userrole
        print(f"Welcome {user.first_name} {user.last_name}")
        print("[L]ogout")
    else:
        print("Welcome guest")
        print("[L]ogin")

    print("[A]dd book")
    print("[D]elete book")

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


def set_guest_user() -> librarian:
    """Set the defautl user as a librarian with name 'guest user'."""
    return add_librarian("guest", "user")


def login() -> librarian:
    """Login w/ username and passwort."""
    name = input("enter user name: ")
    # passwort = input("enter passwort: ")
    # @todo passwort check
    # @todo load user data
    return add_librarian("", name)


def logout() -> librarian:
    """Logs out current user by setting it to guest user."""
    return set_guest_user()


if __name__ == "__main__":
    run_program = True
    current_user = set_guest_user()

    while run_program:
        show_main_menue(current_user)
        command = input("Your Choice: ").upper()
        if len(command) > 1:
            print("Commands consist of single letters only.")
        match command:
            case "A":
                print("not implemented")
            case "C":
                print("not implemented")
            case "D":
                print("not implemented")
            case "L":
                if current_user.first_name == "guest":  # @fix w/ userrole
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
