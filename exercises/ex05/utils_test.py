"""Tests the only_evens, sub, and concat functions."""

__author__ = "730489697"


from exercises.ex05.utils import only_evens, sub, concat


def test_only_evens_empty() -> None:
    lst: list[int] = []
    assert only_evens(lst) == []


def test_only_evens_single_item() -> None:
    lst: list[int] = [2]
    assert only_evens(lst) == [2]


def test_only_evens_many_items() -> None:
    lst: list[int] = [1, 2, 3]
    assert only_evens(lst) == [2]


def test_sub_empty() -> None:
    sub_lst: list[int] = []
    x = 1
    y = 3
    assert sub(lst) == []


def test_sub_single_item() -> None:
    sub_lst: list[int] = [2]
    x = 1
    y = 3
    assert sub(lst) == []


def test_sub_many_items() -> None:
    sub_lst: list[int] = [1, 2, 3, 4]
    x = 1
    y = 3
    assert sub(lst) == [2, 3]


def test_concat_empty() -> None:
    result: list[int] = []
    x: list[int] = []
    y: list[int] = []
    assert concat(lst) == []


def test_concat_single_item() -> None:
    result: list[int] = []
    x: list[int] = [1]
    y: list[int] = [2]
    assert concat(lst) == [1, 2]


def test_concat_many_items() -> None:
    result: list[int] = []
    x: list[int] = [1, 2, 3]
    y: list[int] = [4, 5, 6]
    assert concat(lst) == [1, 2, 3, 4, 5, 6]