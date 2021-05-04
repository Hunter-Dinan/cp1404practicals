"""Unreliable Car class."""

from car import Car
import random


class UnreliableCar(Car):
    """Specialised version of a Car class that focuses on reliability."""
    def __init__(self, name, fuel, reliability: float):
        """Initialise an Unreliable car instance."""
        super().__init__(name, fuel)
        self.reliability = float(reliability)

    def drive(self, distance):
        """Drive like parent car but based on reliability attribute."""
        random_number = random.randint(0, 100)
        # only drive the car if that number is less than the car's reliability.
        if random_number < self.reliability:
            distance_driven = super().drive(distance)
        else:
            distance_driven = 0
        return distance_driven
