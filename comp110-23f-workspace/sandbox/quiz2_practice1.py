"""Odd and Even"""

def odd_and_even(int_list: list[int]) -> list[int]:
    """Returns a list of odd numbers that also have an even index."""
    output_list: list[int] = []
    for index in range(len(int_list)):
        if index % 2 == 0 and int_list[index] % 2 != 0:
            output_list.append(int_list[index])
    return output_list

print(odd_and_even([0, 1, 2, 3, 4, 5]))
print(odd_and_even([1, 2, 3, 4, 6, 5]))