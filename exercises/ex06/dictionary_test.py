"""Tests the invert, favorite_color, and count functions."""

__author__ = "730489697"


from exercises.ex06.dictionary import invert, favorite_color, count
# Imports the functions from dictionary.py so that it can test each.


def test_invert_empty() -> None:
    """Tests if the invert function works when the dictionary is empty."""
    data: dict[str, str] = dict()
    assert invert(data) == dict()


def test_invert_items() -> None:
    """Tests if the invert function works when the dictionary is normal."""
    data: dict[str, str] = dict({'a': 'z', 'b': 'y', 'c': 'x'})
    assert invert(data) == dict({'z': 'a', 'y': 'b', 'x': 'c'})


def test_invert_repeated_items() -> None:
    """Tests if the invert function works when the inverted dictionary has repeated keys."""
    data: dict[str, str] = dict({'a': 'z', 'b': 'z', 'c': 'x'})
    assert invert(data) == KeyError


def test_favorite_color_empty() -> None:
    """Tests if the favorite_color function works when the dictionary is empty."""
    data: dict[str, str] = dict()
    assert favorite_color(data) == ''


def test_favorite_color_items() -> None:
    """Tests if the favorite_color function works when there is one favorite color."""
    data: dict[str, str] = dict({"Marc": "yellow", "Ezri": "blue", "Kris": "blue"})
    assert favorite_color(data) == 'blue'


def test_favorite_color_two_repeated_items() -> None:
    """Tests if the favorite_color function works when the dictionary has multiple favorite colors."""
    data: dict[str, str] = dict({"Marc": "yellow", "Ezri": "yellow", "Kris": "blue", "Joey": "blue"})
    assert favorite_color(data) == 'yellow'


def test_count_empty() -> None:
    """Tests if the count function works when the dictionary is empty."""
    x: list[str] = []
    assert count(x) == dict()


def test_count_items() -> None:
    """Tests if the count function works when the dictionary is normal."""
    x: list[str] = ['hi', 'hi', 'bye']
    assert count(x) == dict({'hi': 2, 'bye': 1})


def test_count_repeated_items() -> None:
    """Tests if the count function works when the inverted dictionary has repeated keys."""
    x: list[str] = ['hi', 'hi', 'bye', 'bye']
    assert count(x) == dict({'hi': 2, 'bye': 2})