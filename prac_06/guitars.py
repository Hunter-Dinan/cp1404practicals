"""Create list of user's guitars."""

from guitar import Guitar


def main():
    """Create list of user's guitars and display them."""
    guitars = []

    print("My Guitars!")
    is_input_empty = False
    while not is_input_empty:
        name = input("Name: ")
        if name == "":
            is_input_empty = True
        else:
            year_created = input("Year: ")
            cost = input("Cost: ")
            guitar = Guitar(name, year_created, cost)
            guitars.append(guitar)
            print("{guitar} added.".format(guitar=guitar))
            print()
    print()
    display_guitars()


def display_guitars(guitars: list):
    """Displays guitar list."""
    print("These are my guitars:")
    for i, guitar in enumerate(guitars):
        vintage_string = ""
        if guitar.is_vintage():
            vintage_string = " (vintage)"
        print("Guitar {}: {:>20} ({}), worth $e{:10,.2f}{}".format(i + 1, guitar.name, guitar.year, guitar.cost,
                                                                   vintage_string))


main()
