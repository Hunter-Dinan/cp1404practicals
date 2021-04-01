"""Store user's emails and names in a dictionary."""


def main():
    """Create dictionary for emails and names."""
    email_to_name = {}
    email = input("Email: ")
    while email != "":
        name = get_name_from_email(email)
        valid_name = input("Is your name {}? (Y/n)".format(name))
        if valid_name.lower() != "y" and valid_name.lower() != "":
            name = input("Name: ").title()
        email_to_name[email] = name.title()
        email = input("Email: ")
    print()
    display_names_and_emails(email_to_name)


def get_name_from_email(email):
    """Get name from email address."""
    name = email.split("@")[0]
    if "." in name:
        names = name.split(".")
        name = " ".join(names)
    return name.title()


def display_names_and_emails(email_to_name: dict):
    """Display names and their corresponding emails."""
    for email, name in email_to_name.items():
        print("{} ({})".format(name, email))


main()
