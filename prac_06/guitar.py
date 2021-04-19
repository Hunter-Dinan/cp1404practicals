"""Class defining a guitar."""

CURRENT_YEAR = 2021     # Improvement: Use computer's internal clock
VINTAGE_AGE = 50


class Guitar:
    """Represents a Guitar object."""

    def __init__(self, name="", year=0, cost=0):
        """Initialise a Guitar instance."""
        self.name = name
        self.year = int(year)
        self.cost = float(cost)

    def __str__(self):
        """String form of the instance."""
        return "{} ({}) : ${:,.2f}".format(self.name, self.year, self.cost)

    def get_age(self):
        """Get age of guitar."""
        age = CURRENT_YEAR - self.year
        return age

    def is_vintage(self):
        """Determine if a guitar is vintage or not based on VINTAGE_AGE."""
        age = self.get_age()
        return age >= VINTAGE_AGE
