"""module docstring."""

from taxi import Taxi


class SilverServiceTaxi(Taxi):
    """docstring"""
    flagfall = 4.5

    def __init__(self, name, fuel, fanciness: float):
        """docstring"""
        super().__init__(name, fuel)
        self.fanciness = float(fanciness)
        self.price_per_km = self.fanciness * self.price_per_km

    def start_fare(self):
        """docstring"""
        super().start_fare()

    def get_fare(self):
        """docstring"""
        distance_fare = super().get_fare()
        total_fare = distance_fare + self.flagfall
        return total_fare

    def __str__(self):
        """docstring"""
        return "{} plus flagfall of ${:.2f}".format(super().__str__(), self.flagfall)
