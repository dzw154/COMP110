"""Summing the elements of a list using different loops."""

__author__ = "730677774"


def w_sum(vals: list[float]) -> float:
    """Sums up all numbers in a given list using a while loop."""
    sum: float = 0.0
    val_index: int = 0
    if len(vals) == 0:
        return 0.0
    else:
        while val_index < len(vals):
            sum += vals[val_index]
            val_index += 1
    return sum


def f_sum(vals: list[float]) -> float:
    """Sums up all numbers in a given list using a for loop."""
    sum: float = 0.0
    if len(vals) == 0:
        return 0.0
    else:
        for num in vals:
            sum += num
    return sum


def f_range_sum(vals: list[float]) -> float:
    """Sums up all numbers in a given loop using a for loop and the range function."""
    sum: float = 0.0
    if len(vals) == 0:
        return 0.0
    else:
        for index in range(0, len(vals)):
            sum += vals[index]
    return sum

# test: list[float] = [1.0, 3.0, 5.0]
# test2: list[float] = []

# print(w_sum(test))
# print(w_sum(test2))
# print(f_sum(test))
# print(f_sum(test2))
# print(f_range_sum(test))
# print(f_range_sum(test2))