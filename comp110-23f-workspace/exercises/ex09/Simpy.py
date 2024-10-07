"""Utility class for numerical operations."""

# python -m tools.submission exercises/ex09

from __future__ import annotations

from typing import Union

__author__ = "YOUR PID HERE"


class Simpy:
    """The Simpy class is a simpler implementation of NumPy."""
    values: list[float]

    # TODO: Your constructor and methods will go here.

    def __init__(self, float_list: list[float]) -> None:
        """Initializes the value of self.values to float_list."""
        self.values = float_list
    
    def __str__(self) -> str:
        """Printing a Simpy object will be in the format 'Simpy(...)' where the ellipses are replaced by the values of self.values."""
        return f"Simpy({self.values})"
    
    def fill(self, obj: float, num: int) -> None:
        """Fills 'self.values' with 'obj' 'num' times."""
        self.values = []
        for item in range(num):
            self.values.append(obj)

    def arange(self, start: float, stop: float, step: float = 1.0) -> None:
        """Fills self.values with numbers ranging from 'start' to 'stop', not including 'stop', incrementing by 'step.'."""
        assert step != 0.0, "Step cannot be 0."
        holder: float = 0.0
        while holder < abs((stop - start) / step):
            self.values.append(start + step * holder)
            holder += 1

    def sum(self) -> float:
        """Returns the sum of all items within self.values."""
        sum: float = 0
        for item in self.values:
            sum += item
        return sum
    
    def __add__(self, other: Union[float, Simpy]) -> Simpy:
        """Creates a new Simpy object from adding 'other' to each value in self.values or combining the corresponding values between the two Simpy objects."""
        new_values: list[float] = []
        if isinstance(other, float):
            for item in self.values:
                new_values.append(item + other)
        else:
            assert len(self.values) == len(other.values), "Both Simpy objects must be of identical length."
            for index in range(len(self.values)):
                new_values.append(self.values[index] + other.values[index])
        return Simpy(new_values)
    
    def __pow__(self, power: Union[float, Simpy]) -> Simpy:
        """Creates a new Simpy object that is the result of raising the first Simpy object to 'power' or raising each value in self.values to the power of the corresponding value in the power Simpy."""
        new_values: list[float] = []
        if isinstance(power, float):
            for item in self.values:
                new_values.append(item ** power)
        else:
            assert len(self.values) == len(power.values), "Both Simpy objects must be of identical length."
            for index in range(len(self.values)):
                new_values.append(self.values[index] ** power.values[index])
        return Simpy(new_values)
    
    def __eq__(self, other: Union[float, Simpy]) -> list[bool]:
        """Checks if the items in two Simpy's are equal to each other or if the items in one Simpy are equal to a float."""
        bool_list: list[bool] = []
        if isinstance(other, float):
            for item in self.values:
                if item == other:
                    bool_list.append(True)
                else:
                    bool_list.append(False)
        else:
            assert len(self.values) == len(other.values), "Both Simpy objects must be of identical length."
            for index in range(len(self.values)):
                if self.values[index] == other.values[index]:
                    bool_list.append(True)
                else:
                    bool_list.append(False)
        return bool_list
    
    def __gt__(self, other: Union[float, Simpy]) -> list[bool]:
        """Checks if the items in one Simpy are greater than the corresponding items in another Simpy or if the items in one Simpy are greater than a float."""
        bool_list: list[bool] = []
        if isinstance(other, float):
            for item in self.values:
                if item > other:
                    bool_list.append(True)
                else:
                    bool_list.append(False)
        else:
            assert len(self.values) == len(other.values), "Both Simpy objects must be of identical length."
            for index in range(len(self.values)):
                if self.values[index] > other.values[index]:
                    bool_list.append(True)
                else:
                    bool_list.append(False)
        return bool_list
    
    def __getitem__(self, rhs: Union[int, list[bool]]) -> Union[float, Simpy]:
        """Allows access to specific items in self.values through indexes or filtering the Simpy."""
        if isinstance(rhs, int):
            return self.values[rhs]
        else:
            new_list: list[float] = []
            for index in range(len(self.values)):
                if rhs[index]:
                    new_list.append(self.values[index])
            return new_list