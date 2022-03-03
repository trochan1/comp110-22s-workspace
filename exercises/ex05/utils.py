"""EX05 - Experimenting with list utility functions!"""

__author__ = "730489697"


def only_evens(x: list[int]) -> list[int]:
    """Returns a list containing only the elements of the input list that are even."""
    lst: list[int] = []
    # I created a lst variable so that my x list is not mutated.
    i = 0
    # This counter variable will help check each index in the list.
    while (i < len(x)):
        if (x[i] % 2 == 0):
            # This if function checks to see whether each individual element in the input list is even or odd.
            lst.append(x[i])
            # This adds each element from the input function that is even to the empty lst list.
        i = i + 1
    return lst


def sub(x: list[int], y: int, z: int) -> list[int]:
    """Generates a list that is a subset of the given list."""
    sub_lst = []
    # I created a sub_lst variable so that the input list x is not mutated.
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
        # y increases by 1 each time so that the while loop eventually reaches an end point (when y is greater than z)
    return sub_lst


def concat(x: list[int], y: list[int]):
    result = x
    # I created a result variable so that the input lists x and y are not mutated.
    if x == [] and y == []:
        return x and y
    for i in y:
        result.append(i)
        # This appends each element in the y list to the result list, which is just a repeat of the input list x.
    return result