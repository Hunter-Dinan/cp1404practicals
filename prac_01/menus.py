name = str(input("Enter name: "))
menu = """(H)ello
(G)oodbye
(Q)uit"""
print(menu)
menu_input = str(input())

while menu_input != "Q":
    if menu_input == "H":
        print("Hello {}".format(name))
    elif menu_input == "G":
        print("Goodbye {}".format(name))
    else:
        print("Invalid input")
    print(menu)
    menu_input = str(input())
print("Finished")
