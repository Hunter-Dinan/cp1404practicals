"""Class defining a Programming Language."""


class ProgrammingLanguage:
    """Represents a Programming Language object."""

    def __init__(self, name, typing, reflection, year_created):
        """Initialise a Programming Language instance."""
        self.name = name
        self.typing = typing
        self.reflection = bool(reflection)
        self.year_created = int(year_created)

    def __str__(self):
        """Return string form of the Programming Language instance."""
        return "{}, {} Typing, Reflection={}, First appeared in {}".format(self.name, self.typing,
                                                                           self.reflection, self.year_created)

    def is_dynamic(self):
        """Determine if the language is dynamically typed."""
        return self.typing == "Dynamic"
