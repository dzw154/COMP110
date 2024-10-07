"""File to define Bear class."""


class Bear:
    """Class for simulating bears."""
    age: int
    hunger_score: int
    
    def __init__(self):
        """Bear object constructor initializes age and hunger_score to 0."""
        self.age = 0
        self.hunger_score = 0
        return None
    
    def one_day(self):
        """Simulates the passage of one day for a bear."""
        self.age += 1
        self.hunger_score -= 1
        return None

    def eat(self, num_fish: int) -> None:
        """Increases the bear's hunger score based on how many fish it ate."""
        self.hunger_score += num_fish
        return None