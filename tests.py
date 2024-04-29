# tests
import libraryvault as liva

assert (
    isinstance(liva.add_librarian("Vorname", "Nachname"), liva.librarian)
) is True, 'error: add_librarian("Vorname", "Nachname")'
assert (
    liva.add_librarian("Vorname", "Nachname").first_name == "Vorname"
) is True, 'error: add_librarian("Vorname")'
assert (
    liva.add_librarian("Vorname", "Nachname").last_name == "Nachname"
) is True, 'error: add_librarian("Nachname")'
