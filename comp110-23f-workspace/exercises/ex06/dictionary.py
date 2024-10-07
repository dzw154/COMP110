"""Dictionary Utility Functions."""

__author__ = "730677774"


def invert(input_dict: dict[str, str]) -> dict[str, str]:
    """Reverses the keys and values in a dictionary."""
    reverse_dict: dict[str, str] = {}
    for key in input_dict:
        if input_dict[key] not in reverse_dict:
            reverse_dict[input_dict[key]] = key
        else:
            raise KeyError("Key already exists in dictionary.")
    return reverse_dict


def favorite_color(input_dict: dict[str, str]) -> str:
    """Finds the color that appears most in a dictionary."""
    colors_dict: dict[str, int] = {}
    max_color: str = ""
    max_int: int = 0
    for key in input_dict:
        if input_dict[key] not in colors_dict:
            colors_dict[input_dict[key]] = 1
        else:
            colors_dict[input_dict[key]] += 1
    for key in colors_dict:
        if colors_dict[key] > max_int:
            max_int = colors_dict[key]
            max_color = key
    return max_color


def count(input_list: list[str]) -> dict[str, int]:
    """Counts the frequencies that items occur in a given list."""
    freq_dict: dict[str, int] = {}
    for item in input_list:
        if item not in freq_dict:
            freq_dict[item] = 1
        else:
            freq_dict[item] += 1
    return freq_dict


def alphabetizer(str_list: list[str]) -> dict[str, list[str]]:
    """Displays ever word that has a certain alphabet character in them."""
    alpha_dict: dict[str, list[str]] = {}
    for word in str_list:
        letter = word[0]
        if letter.lower() not in alpha_dict:
            alpha_dict[letter.lower()] = [word]
        else:
            alpha_dict[letter.lower()].append(word)
    return alpha_dict


def update_attendance(input_dict: dict[str, list[str]], day: str, student: str) -> dict[str, list[str]]:
    """Updates the attendance list for students on certain days of the week."""
    if day not in input_dict:
        input_dict[day] = [student]
    else:
        if student not in input_dict[day]:
            input_dict[day].append(student)
    return input_dict