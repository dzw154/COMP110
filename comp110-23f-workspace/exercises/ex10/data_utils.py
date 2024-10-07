"""Dictionary related utility functions."""

__author__ = "730677774"

# python -m tools.submission exercises/ex10

# Define your functions below

from csv import DictReader


def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read csv file and return as a list of dicts with the headers as the keys."""
    result: list[dict[str, str]] = []
    file_handle = open(filename, "r", encoding="utf8")
    csv_reader = DictReader(file_handle)
    for row in csv_reader:
        result.append(row)
    file_handle.close()
    return result


def column_values(table: list[dict[str, str]], header: str) -> list[str]:
    """Return a list of all values under a specific header."""
    result: list[str] = []
    # loop through each element (dictionary) of the list
    for elem in table:
        # for each dictionary (elem), get the value at key "header" and add that to result
        result.append(elem[header])
    return result


def columnar(table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Reformat data so it's a dictionary with column headers as keys."""
    result: dict[str, list[str]] = {}
    # loop through keys of one row of the table to get the headers
    first_row: dict[str, str] = table[0]
    for key in first_row:
        # for each key (header), make a dictionary entry with all the column values
        result[key] = column_values(table, key)
    return result


def head(base: dict[str, list[str]], rows: int) -> dict[str, list[str]]:
    """Creates a modified version of the base dictionary with only n rows."""
    result: dict[str, list[str]] = {}
    if rows >= len(base): 
        for key in base:
            result[key] = []
            for item in range(len(base)):
                result[key].append(base[key][item])
    else:
        for key in base:
            result[key] = []
            for item in range(rows):
                result[key].append(base[key][item])
    return result


def select(base: dict[str, list[str]], columns: list[str]) -> dict[str, list[str]]:
    """Creates a new dictionary with only the selected columns."""
    result: dict[str, list[str]] = {}
    for item in columns:
        result[item] = base[item]
    return result


def concat(base1: dict[str, list[str]], base2: dict[str, list[str]]) -> dict[str, list[str]]:
    """Combines two tables of data together."""
    result: dict[str, list[str]] = {}
    for item in base1:
        result[item] = base1[item]
    for key, value in base2.items():
        if key in result:
            result[key] = value
        else:
            result[key].extend(value)
    return result


def count(values: list[str]) -> dict[str, int]:
    """Counts how many times each item in values appears."""
    result: dict[str, int] = {}
    for item in values:
        if item in result:
            result[item] += 1
        else:
            result[item] = 1
    return result