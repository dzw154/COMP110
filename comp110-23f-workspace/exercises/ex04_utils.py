"""Ex04 - List Util Functions - Remaking all, max, and is_equal."""

__author__ = "730677774"


def all(int_list: list[int], num: int) -> bool:
    """Checks if the integers in a list of integers it_list are the same as a given integer num."""
    index: int = 0
    if len(int_list) == 0:
        return False
    while index < len(int_list):
        if int_list[index] != num:
            return False
        index += 1
    return True


def max(int_list: list[int]) -> int:
    """Finds the greatest integer in a list of integers int_list."""
    if len(int_list) == 0:
        raise ValueError("max() arg is an empty List")
    max_val: int = int_list[0]
    index: int = 0
    while index < len(int_list):
        if int_list[index] > max_val:
            max_val = int_list[index]
        index += 1
    return max_val


def is_equal(list1: list[int], list2: list[int]) -> bool:
    """Checks if two lists of integers list1 and list2 are deeply equal."""
    if len(list1) != len(list2):
        return False
    index = 0
    while index < len(list1):
        if list1[index] != list2[index]:
            return False
        index += 1
    return True


# print(all([1, 2, 3], 3))
# print(all([1,1,1],1))
# print(all([],1))
# print(max([1, 900, 3, 4, 5, 100]))
# print(is_equal([1, 2, 3],[1, 2, 3]))