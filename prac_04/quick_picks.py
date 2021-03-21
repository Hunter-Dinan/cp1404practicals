import random


def main():
    """Quick Pick Lottery Ticket Generator."""
    number_of_quick_picks = int(input("How many quick picks? "))
    quick_picks = []
    quick_picks = get_quick_picks(quick_picks, number_of_quick_picks)
    sort_quick_picks(quick_picks)
    print_quick_picks(quick_picks)


def get_quick_picks(quick_picks: list, number_of_quick_picks):
    """Generates Quick Pick data."""
    for i in range(0, number_of_quick_picks):
        numbers = []
        for j in range(0, 6):
            # store entire list in ith element of quick_pick_numbers
            number = random.randint(1, 45)
            while number in numbers:
                number = random.randint(1, 45)
            numbers.append(number)
        quick_picks.append(numbers)
    return quick_picks


def sort_quick_picks(quick_picks: list):
    """Sort Quick Pick data in ascending order."""
    for quick_pick in quick_picks:
        quick_pick.sort()


def print_quick_picks(quick_picks: list):
    """Print formatted Quick Pick data."""
    for quick_pick in quick_picks:
        print("{:2} {:2} {:2} {:2} {:2}".format(quick_pick[0], quick_pick[1], quick_pick[2], quick_pick[3], quick_pick[4]))


main()
