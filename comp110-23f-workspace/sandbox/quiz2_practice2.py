"""Value Exists"""

def value_exists(input_dict: dict[str, int], search_int: int) -> bool:
    """Checks if a given value exists in a dictionary."""
    for key in input_dict:
        if input_dict[key] == search_int:
            return True
    return False


dict = {"a":1, "b":2, "c":1}
print(value_exists(dict, 3))