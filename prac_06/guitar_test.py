"""Test Guitar Class functionality."""

from guitar import Guitar


def main():
    """Test Guitar Class functionality."""
    first_guitar = Guitar("Gibson L-5 CES", 1922, 16035.40)
    second_guitar = Guitar("Another Guitar", 2013, 1500.12)

    print("{} get_age() - Expected {}. Got {}".format(first_guitar.name, 99, first_guitar.get_age()))
    print("{} get_age() - Expected {}. Got {}".format(second_guitar.name, 8, second_guitar.get_age()))
    print("{} is_vintage() - Expected {}. Got {}".format(first_guitar.name, True, first_guitar.is_vintage()))
    print("{} is_vintage() - Expected {}. Got {}".format(second_guitar.name, False, second_guitar.is_vintage()))


main()
