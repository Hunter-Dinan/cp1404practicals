MIN_LENGTH = 5

password = input("Enter password with minimum length of {}: ".format(MIN_LENGTH))
while len(password) < MIN_LENGTH:
    print("Invalid password")
    password = input("Enter password: ")

for i in range(0, len(password)):
    print("*", end='')
