"""Tests the only_evens, sub, and concat functions."""

__author__ = "730489697"


from exercises.ex05.utils import only_evens, sub, concat
# Imports the functions from utils.py so that it can test each.


def test_only_evens_empty() -> None:
    """Tests if the only_evens function works when the input list is empty."""
    x: list[int] = []
    assert only_evens(x) == []


def test_only_evens_single_item() -> None:
    """Tests if the only_evens function works when the input list has one element."""
    x: list[int] = [2]
    assert only_evens(x) == [2]


def test_only_evens_many_items() -> None:
    """Tests if the only_evens function works when the input list has multiple elements."""
    x: list[int] = [1, 2, 3]
    assert only_evens(x) == [2]


def test_sub_empty() -> None:
    """Tests if the sub function works when the input list is empty."""
    x: list[int] = []
    y: int = 1
    z: int = 3
    assert sub(x, y, z) == []


def test_sub_single_item() -> None:
    """Tests if the sub function works when the input list has one element."""
    x: list[int] = [2]
    y: int = 1
    z: int = 3
    assert sub(x, y, z) == []


def test_sub_many_items() -> None:
    """Tests if the sub function works when the input list has multiple elements."""
    x: list[int] = [1, 2, 3, 4]
    y: int = 1
    z: int = 3
    assert sub(x, y, z) == [2, 3]


def test_concat_empty() -> None:
    """Tests if the concat function works when the input list is empty."""
    x: list[int] = []
    y: list[int] = []
    assert concat(x, y) == []


def test_concat_single_item() -> None:
    """Tests if the concat function works when the input list has one element."""
    x: list[int] = [1]
    y: list[int] = [2]
    assert concat(x, y) == [1, 2]


def test_concat_many_items() -> None:
    """Tests if the concat function works when the input list has multiple elements."""
    x: list[int] = [1, 2, 3]
    y: list[int] = [4, 5, 6]
    assert concat(x, y) == [1, 2, 3, 4, 5, 6]