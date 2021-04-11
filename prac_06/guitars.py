"""Create list of user's guitars."""

from guitar import Guitar


def main():
    """Displays list of user's guitars."""
    guitars = []

    print("My Guitars!")
    name = input("Name: ")
    while name != "":
        year_created = input("Year: ")
        cost = input("Cost: ")
        guitar = Guitar(name, year_created, cost)
        guitars.append(guitar)
        print("{guitar} added.".format(guitar=guitar))
        print()
        name = input("Name: ")
    print()
    display_guitars(guitars)


def display_guitars(guitars: list):
    """Displays guitar list."""
    print("These are my guitars:")
    for i, guitar in enumerate(guitars):
        vintage_string = " (vintage)" if guitar.is_vintage() else ""
        print("Guitar {}: {:>20} ({}), worth ${:10,.2f}{}".format(i + 1, guitar.name, guitar.year, guitar.cost,
                                                                  vintage_string))


main()
