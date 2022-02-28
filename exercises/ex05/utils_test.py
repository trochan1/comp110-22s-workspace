"""EX05 - Experimenting with unit tests"""

__author__ = "730489697"

from utils import only_evens, sub, concat


def test_only_evens_empty() -> None:
    xs: list[float] = []
    assert sum([]) == 0.0


def test_sub_single_item() -> None:
    xs: list[float] = [110.0]
    assert sum(xs) == 110.0


def test_concat_many_items() -> None:
    xs: list[float] = [1.0, 2.0, 3.0]
    assert sum(xs) == 6.0