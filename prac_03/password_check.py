MIN_LENGTH = 5


def main():
    password = get_password()
    print_asterisk_string(password)


def get_password():
    password = input("Enter password with minimum length of {}: ".format(MIN_LENGTH))
    while len(password) < MIN_LENGTH:
        print("Invalid password")
        password = input("Enter password: ")
    return password


def print_asterisk_string(string):
    for i in range(0, len(string)):
        print("*", end='')


main()
