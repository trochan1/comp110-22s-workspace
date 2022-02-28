"""EX05 - Experimenting with list utility functions!"""

__author__ = "730489697"

lst: list[int] = []

def only_evens(x: list[int]) -> list[int]:
    """Returns a list containing only the elements of the input list that are even."""
    if len(x) == 0:
        return []
    for xs in x:
        if x[xs] % 2 == 0:
            lst.append(xs)
    return lst

def sub(x:list[int], y: int, z: int) -> list[int]:
    """Generates a list that is a subset of the given list."""
    if y < 0:
        y = 0
    if z > len(x):
        z = len(x)
    if y >= len(x):
        return []
    if z == 0:
        return []
    while y < z:
        xs = [x[y], x[z-1]]
        lst.append(xs)
    return lst

def concat(x:list[int], y:list[int]):
    if x == [] and y == []:
        return x and y
    return y.append(x)