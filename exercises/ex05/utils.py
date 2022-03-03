"""EX05 - Experimenting with list utility functions!"""

__author__ = "730489697"


def only_evens(x: list[int]) -> list[int]:
    """Returns a list containing only the elements of the input list that are even."""
    lst: list[int] = []
    i = 0
    while (i < len(x)):
        if (x[i] % 2 == 0):
            lst.append(x[i])
        i = i + 1
    return lst


def sub(x: list[int], y: int, z: int) -> list[int]:
    """Generates a list that is a subset of the given list."""
    sub_lst = []
    if y < 0:
        y = 0
    if z > len(x):
        z = len(x)
    if y >= len(x):
        return []
    if z <= 0:
        return []
    if len(x) == 0:
        return []
    while y < z:
        sub_lst.append(x[y])
        y += 1
    return sub_lst


def concat(x: list[int], y: list[int]):
    result = x
    if x == [] and y == []:
        return x and y
    for i in y:
        result.append(i)
    return result