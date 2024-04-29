class user_role:
    def __init__(self, first_name, last_name) -> None:
        self.first_name = first_name
        self.last_name = last_name


class library_user(user_role):
    def __init__(self, first_name, last_name) -> None:
        super().__init__()


class librarian(user_role):
    def __init__(self, first_name, last_name) -> None:
        super().__init__(first_name, last_name)
