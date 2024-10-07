"""File to define River class."""

from exercises.ex08.fish import Fish
from exercises.ex08.bear import Bear

__author__ = "730677774"


class River:
    """Class for simulating a river."""
    def __init__(self, num_fish: int, num_bears: int):
        """New River with num_fish Fish and num_bears Bears."""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for x in range(0, num_fish):
            self.fish.append(Fish())
        for x in range(0, num_bears):
            self.bears.append(Bear())

    def check_ages(self):
        """Checks the ages of all fish and bears and removes them from the population if the fish are over 3 days old or if the bears are over 5 days old."""
        new_bear: list[Bear] = []
        new_fish: list[Fish] = []
        for olfactore in self.fish:
            if olfactore.age <= 3:
                new_fish.append(olfactore)
        for ursa in self.bears:
            if ursa.age <= 5:
                new_bear.append(ursa)
        self.bears = new_bear
        self.fish = new_fish
        return None

    def bears_eating(self):
        """If there are 5 or more fish in the river, a bear will eat 3 fish, removing 3 fish from the population."""
        for ursa in self.bears:
            if len(self.fish) >= 5:
                ursa.eat(3)
                self.remove_fish(3)
        return None
    
    def check_hunger(self):
        """If a bear has negative hunger, it dies of starvation and is removed from the population."""
        for ursa in range(len(self.bears) - 1):
            if self.bears[ursa].hunger_score < 0:
                self.bears.pop(ursa)
        return None
        
    def repopulate_fish(self):
        """Increases the fish population by 4 for every pair of fish."""
        for count in range(len(self.fish) // 2):
            self.fish.append(Fish())
            self.fish.append(Fish())
            self.fish.append(Fish())
            self.fish.append(Fish())
        return None
    
    def repopulate_bears(self):
        """Increases the bear population by 1 for every pair of bears."""
        for bear in range(len(self.bears) // 2):
            self.bears.append(Bear())
        return None
    
    def view_river(self):
        """Allows the user to view the river statistics."""
        print(f"\n~~~ Day {self.day}: ~~~\nFish population: {len(self.fish)}\nBear population: {len(self.bears)}")
        return None
            
    def one_river_day(self):
        """Simulate one day of life in the river."""
        # Increase day by 1
        self.day += 1
        # Simulate one day for all Bears
        for bear in self.bears:
            bear.one_day()
        # Simulate one day for all Fish
        for fish in self.fish:
            fish.one_day()
        # Simulate Bear's eating
        self.bears_eating()
        # Remove hungry Bear's from River
        self.check_hunger()
        # Remove old Fish and Bear's from River
        self.check_ages()
        # Simulate Fish repopulation
        self.repopulate_fish()
        # Simulate Bear repopulation
        self.repopulate_bears()
        # Visualize River
        self.view_river()
    
    def one_river_week(self):
        """Simulates the passing of 1 week in the river."""
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()
    
    def remove_fish(self, amount: int) -> None:
        """Removes amount fish from the population. The fish removed are at the 0th index of self.fish."""
        for x in range(amount):
            self.fish.pop(0)
        return None