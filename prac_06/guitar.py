"""Class defining a guitar."""

CURRENT_YEAR = 2021


class Guitar:
    """Represents a Guitar object."""

    def __init__(self, name="", year=0, cost=0):
        """Initialise a Guitar instance."""
        self.name = name
        self.year = int(year)
        self.cost = float(cost)

    def __str__(self):
        """String form of the instance."""
        return "{} ({}) : ${}".format(self.name, self.year, self.cost)
# TODO - edit the __str__ function to use decimal places and 20 spaces for name

    def get_age(self):
        age = CURRENT_YEAR - self.year
        return age

    def is_vintage(self):
        age = self.get_age()
        return age >= 50
