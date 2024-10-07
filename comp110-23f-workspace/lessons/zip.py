"""Combining two lists into a dictionary."""

__author__ = "730677774"


def zip(list1: list[str], list2: list[int]) -> dict[str, int]:
    """Combines two lists into a dictionary."""
    dictionary: dict[str, int] = {}
    if (list1 == [] or list2 == []) or (len(list1) != len(list2)):
        return dictionary
    else:
        for item in range(len(list1)):
            dictionary[list1[item]] = list2[item]
    return dictionary
