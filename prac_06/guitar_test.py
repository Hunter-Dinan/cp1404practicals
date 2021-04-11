"""Test Guitar Class functionality."""

from guitar import Guitar


def main():
    """Test Guitar Class functionality."""
    first_guitar = Guitar("Gibson L-5 CES", 1922, 16035.40)
    second_guitar = Guitar("Another Guitar", 2013, 1500.12)

    print("{} get_age() - Expected 99. Got {}".format(first_guitar.name, first_guitar.get_age()))
    print("{} get_age() - Expected 8. Got {}".format(second_guitar.name, second_guitar.get_age()))
    print("{} is_vintage() - Expected True. Got {}".format(first_guitar.name, first_guitar.is_vintage()))
    print("{} is_vintage() - Expected False. Got {}".format(second_guitar.name, second_guitar.is_vintage()))
    print(first_guitar)


main()
