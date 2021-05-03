"""Unreliable Car class."""

from car import Car


class UnreliableCar(Car):
    def __init__(self, name, fuel):
        super().__init__(name, fuel)
