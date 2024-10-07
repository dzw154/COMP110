"""Test my zip function."""

import zip

__author__ = "730677774"


def test_both_empty() -> None:
    """Tests what happens if both lists are empty."""
    empty_int_list: list[int] = []
    empty_str_list: list[str] = []
    assert zip.zip(empty_str_list, empty_int_list) == {}


def test_different_lengths() -> None:
    """Tests what hapens if the lists are of different lengths."""
    big_int_list: list[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    str_list: list[str] = ["a", "b", "c"]
    assert zip.zip(str_list, big_int_list) == {}


def test_same_length() -> None:
    """Tests what happens when the lists are of the same length."""
    str_list: list[str] = ["a", "b", "c"]
    small_int_list: list[int] = [1, 2, 3]
    assert zip.zip(str_list, small_int_list) == {"a": 1, "b": 2, "c": 3}