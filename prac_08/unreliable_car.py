"""Unreliable Car class."""

from car import Car
import random


class UnreliableCar(Car):
    """docstring."""
    def __init__(self, name, fuel, reliability: float):
        """docstring"""
        super().__init__(name, fuel)
        self.reliability = float(reliability)

    def drive(self, distance):
        """docstring"""
        random_number = random.randint(0, 100)
        # only drive the car if that number is less than the car's reliability.
        if random_number < self.reliability:
            distance_driven = super().drive(distance)
        else:
            distance_driven = 0
        return distance_driven
