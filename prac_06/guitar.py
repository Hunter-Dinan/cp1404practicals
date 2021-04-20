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
        """Return string form of the Guitar instance."""
        return "{} ({}) : ${:,.2f}".format(self.name, self.year, self.cost)

    def get_age(self):
        """Get age of guitar."""
        return CURRENT_YEAR - self.year

    def is_vintage(self):
        """Determine if a guitar is vintage or not based on VINTAGE_AGE."""
        return self.get_age() >= VINTAGE_AGE
