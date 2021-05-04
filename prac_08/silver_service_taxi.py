"""SilverServiceTaxi class, specialised version of Taxi"""

from taxi import Taxi


class SilverServiceTaxi(Taxi):
    """SilverServiceTaxi, Specialised version of a Taxi class."""
    flagfall = 4.5

    def __init__(self, name, fuel, fanciness: float):
        """Initiate SilverServiceTaxi instance."""
        super().__init__(name, fuel)
        self.fanciness = float(fanciness)
        self.price_per_km = self.fanciness * self.price_per_km

    def get_fare(self):
        """Return the price for a taxi trip plus flagfall."""
        distance_fare = super().get_fare()
        if self.current_fare_distance == 0:
            total_fare = distance_fare
        else:
            total_fare = distance_fare + self.flagfall
        return total_fare

    def __str__(self):
        """Return string representation of SilverServiceTaxi instance."""
        return "{} plus flagfall of ${:.2f}".format(super().__str__(), self.flagfall)
