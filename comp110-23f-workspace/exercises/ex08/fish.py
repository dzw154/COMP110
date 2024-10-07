"""File to define Fish class."""


class Fish:
    """Class to simulate fish."""
    age: int
    
    def __init__(self):
        """Fish object constructor intializes age to 0."""
        self.age = 0
        return None

    def one_day(self):
        """Simulates the passage of 1 day for a fish."""
        self.age += 1
        return None