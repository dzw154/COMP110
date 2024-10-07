"""Testing Dictionary Functions."""

import pytest
from exercises.ex06.dictionary import invert, favorite_color, count, alphabetizer, update_attendance

__author__ = "730677774"


def test_invert1() -> None:
    """Tests the invert function from py."""
    test_dict: dict[str, str] = {"word1": "a", "word2": "b", "word3": "c"}
    assert invert(test_dict) == {"a": "word1", "b": "word2", "c": "word3"}


def test_invert2() -> None:
    """Tests the invert function from py."""
    with pytest.raises(KeyError):
        test_dict: dict[str, str] = {"word1": "a", "word2": "a", "word3": "c"}
        invert(test_dict)


def test_invert3() -> None:
    """Tests the invert function from py."""
    test_dict: dict[str, str] = {}
    assert invert(test_dict) == {}


def test_favorite_color1() -> None:
    """Tests the favorite_color function from py."""
    test_dict: dict[str, str] = {"word1": "a", "word2": "b", "word3": "c"}
    assert favorite_color(test_dict) == "a"


def test_favorite_color2() -> None:
    """Tests the favorite_color function from py."""
    test_dict: dict[str, str] = {"word1": "a", "word2": "a", "word3": "c"}
    assert favorite_color(test_dict) == "a"


def test_favorite_color3() -> None:
    """Tests the favorite_color function from py."""
    test_dict: dict[str, str] = {}
    assert favorite_color(test_dict) == ""


def test_count1() -> None:
    """Tests the count function from py."""
    test_list: list[str] = ["a", "a", "a", "a", "b", "b", "c", "d", "e", "e", "e", "e", "f"]
    assert count(test_list) == {"a": 4, "b": 2, "c": 1, "d": 1, "e": 4, "f": 1}


def test_count2() -> None:
    """Tests the count function from py."""
    test_list: list[str] = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m"]
    assert count(test_list) == {"a": 1, "b": 1, "c": 1, "d": 1, "e": 1, "f": 1, "g": 1, "h": 1, "i": 1, "j": 1, "k": 1, "l": 1, "m": 1}


def test_count3() -> None:
    """Tests the count function from py."""
    test_list: list[str] = []
    assert count(test_list) == {}


def test_alphabetizer1() -> None:
    """Tests the alphabetize function from py."""
    test_list: list[str] = ["cat", "apple", "boy", "angry", "bad", "car"]
    assert alphabetizer(test_list) == {'c': ['cat', 'car'], 'a': ['apple', 'angry'], 'b': ['boy', 'bad']}


def test_alphabetizer2() -> None:
    """Tests the alphabetize function from py."""
    test_list: list[str] = ["six", "words", "that", "I", "just", "say"]
    assert alphabetizer(test_list) == {'s': ['six', 'say'], 'w': ['words'], 't': ['that'], 'i': ['I'], 'j': ['just']}


def test_alphabetizer3() -> None:
    """Tests the alphabetize function from py."""
    test_list: list[str] = []
    assert alphabetizer(test_list) == {}


def test_update_attendance1() -> None:
    """Tests the update_attendance function from py."""
    test_dict: dict[str, list[str]] = {"Monday": ["Vrinda", "Kaleb"], "Tuesday": ["Alyssa"]}
    assert update_attendance(test_dict, "Wednesday", "student1") == {"Monday": ["Vrinda", "Kaleb"], "Tuesday": ["Alyssa"], "Wednesday": ["student1"]}


def test_update_attendance2() -> None:
    """Tests the update_attendance function from py."""
    test_dict: dict[str, list[str]] = {"Monday": ["Vrinda", "Kaleb"], "Tuesday": ["Alyssa"]}
    assert update_attendance(test_dict, "Tuesday", "Alyssa") == {"Monday": ["Vrinda", "Kaleb"], "Tuesday": ["Alyssa"]}


def test_update_attendance3() -> None:
    """Tests the update_attendance function from py."""
    test_dict: dict[str, list[str]] = {}
    assert update_attendance(test_dict, "Wednesday", "student1") == {"Wednesday": ["student1"]}