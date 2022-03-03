"""EX06 - Experimenting with dictionary functions!"""

__author__ = "730489697"


def invert(data: dict[str, str]) -> dict[str, str]:
    """The function gets a dictionary and inverts the data so that the keys become values and vice versa."""
    result: dict[str, str] = dict()
    for key in data:
        if data[key] in result:
            raise KeyError
        result[data[key]] = key
    return result


def favorite_color(data: dict[str, str]) -> str:
    """The function gets a dictionary and returns the color that appears most frequently."""
    count: dict[str, int] = dict()
    result: str = ""
    for key in data:
        if result == "":
            result = data[key]
        if data[key] in count:
            count[data[key]] += 1
        else:
            count[data[key]] = 1
    for key in count:
        if count[key] > count[result]:
            result = key
    return result
    

def count(x: list[str]) -> dict[str, int]:
    dictionary = dict()
    for item in x:
        if (item in dictionary):
            dictionary[item] += 1
        else:
            dictionary[item] = 1
    return dictionary