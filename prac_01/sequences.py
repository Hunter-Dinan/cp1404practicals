x = int(input("Enter a number for x: "))
y = int(input("Enter a number for y: "))
menu = """A: Show the even numbers from x to y
B: Show the odd numbers from x to y
C: Show the squares from x to y
Q: Exit the program"""
print(menu)
menu_input = str(input())
x_y_range = range(0, y-x)

while menu_input != "Q":
    if menu_input == "A":
        # Printing even numbers between x and y
        for i in range(x, y+1):
            i_remainder = i % 2
            if i_remainder == 0:
                print(i, end=' ')
        print()
    elif menu_input == "B":
        # Printing odd numbers between x and y
        for i in range(x, y + 1):
            i_remainder = i % 2
            if i_remainder == 1:
                print(i, end=' ')
        print()
    elif menu_input == "C":
        # Printing square numbers between x and y
        # TODO - Could not figure this out
        print("squares")
    else:
        print("Invalid input")
    print(menu)
    menu_input = str(input())

print("Finished")