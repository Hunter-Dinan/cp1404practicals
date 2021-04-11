"""Class defining a Programming Language."""


class ProgrammingLanguage:
    """Represents a Programming Language object."""
    def __init__(self, name, typing, reflection, year_created):
        """Initialise a ProgrammingLanguage instance."""
        self.name = name
        self.typing = typing
        self.reflection = bool(reflection)
        self.year_created = int(year_created)

    def __str__(self):
        """String form of the instance."""
        return "{}, {} Typing, Reflection={}, First appeared in {}".format(self.name, self.typing,
                                                                           self.reflection, self.year_created)

    def is_dynamic(self):
        return self.typing == "Dynamic"
