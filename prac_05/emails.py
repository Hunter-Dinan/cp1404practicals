"""Store user's emails and names."""

email_to_name = {}
email = input("Email: ")
while email != "":
    name = email.split("@")[0]
    email_to_name[email] = name.title()
    if "." in email_to_name[email]:
        names = email_to_name[email].split(".")
        name = " ".join(names)
        email_to_name[email] = name
    valid_name = input("Is your name {}? (Y/n)".format(email_to_name[email]))
    if valid_name.lower() == "n":
        name = input("Name: ").title()
        email_to_name[email] = name.title()
    elif valid_name.lower() == "no":
        name = input("Name: ").title()
        email_to_name[email] = name.title()
    print(email_to_name)
    email = input("Email: ")

print()
for email, name in email_to_name.items():
    print("{} ({})".format(name, email))
