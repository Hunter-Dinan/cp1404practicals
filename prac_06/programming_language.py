"""Class defining a Programming Language."""


class ProgrammingLanguage:
    """Represents a Programming Language object."""
    def __init__(self, name, typing, reflection, year_created):
        """Initialise a ProgrammingLanguage instance."""
        self.name = name
        self.typing = typing.title()
        self.reflection = reflection.title()
        self.year_created = int(year_created.title())

    def is_dynamic(self):
        return self.typing == "Dynamic"
