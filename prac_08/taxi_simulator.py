"""Taxi simulator program using Taxi and SilverServiceTaxi classes."""

from taxi import Taxi
from silver_service_taxi import SilverServiceTaxi

MENU = """q)uit, c)hoose taxi, d)rive"""


def main():
    """Taxi Simulator, the user chooses a taxi to drive and
    how far they want to drive. The fare for each trip is
    added to the bill until the user quits the program."""
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    current_taxi = None
    bill = 0

    print("Let's drive!")
    print(MENU)
    menu_input = input(">>> ").lower()
    while menu_input != 'q':
        if menu_input == 'c':
            current_taxi = choose_taxi(taxis)
        elif menu_input == 'd':
            if current_taxi is None:
                print("No taxi selected, choose a taxi first!")
            else:
                drive_taxi(current_taxi)
        else:
            print("Invalid input, try again")
        bill = calculate_total_bill(taxis)
        print("Bill to date: ${:.2f}".format(bill))
        print(MENU)
        menu_input = input(">>> ").lower()

    bill = calculate_total_bill(taxis)
    print("Total trip cost: ${:.2f}".format(bill))
    display_taxis(taxis)


def choose_taxi(taxis: list):
    """Choose taxi from list of taxis."""
    print("Taxis available:")
    display_taxis(taxis)
    taxi_index_input = int(input("Choose taxi: "))
    current_taxi = taxis[taxi_index_input]
    return current_taxi


def display_taxis(taxis: list):
    """Display enumerated list of taxis."""
    for i, taxi in enumerate(taxis):
        print("{} - {}".format(i, taxi))


def drive_taxi(taxi: object):
    """Drive taxi the inputted distance."""
    distance = float(input("Drive how far? "))
    taxi.drive(distance)
    print("Your {} cost you ${:.2f}".format(taxi.name, taxi.get_fare()))


def calculate_total_bill(taxis: list):
    """Calculate the total bill for all taxi fares."""
    bill = 0
    for taxi in taxis:
        bill += taxi.get_fare()
    return bill


main()
