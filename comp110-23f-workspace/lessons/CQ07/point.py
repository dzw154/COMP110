"""Creates a point class."""

from __future__ import annotations

__author__ = "730677774"


class Point:
    """Creates a new class of objects called points, which have an x and y value."""
    x: float
    y: float

    def __init__(self, x_init: float = 0.0, y_init: float = 0.0) -> None:
        """Constructs a point object at a given x and y value."""
        self.x = x_init
        self.y = y_init

    def __str__(self) -> str:
        """Changes how the objects are printed."""
        return f"x: {self.x}; y: {self.y}"

    def scale_by(self, factor: int) -> None:
        """Scales the x and y values of a point by a factor."""
        self.x *= factor
        self.y *= factor
    
    def __mul__(self, factor: int | float) -> Point:
        """Creates a new point with x and y values that were scaled up from a previous point."""
        return Point(self.x * factor, self.y * factor)
    
    def __add__(self, factor: int | float) -> Point:
        """Creates a new point with x and y values that added from previous point."""
        return Point(self.x + factor, self.y + factor)