"""EX06 - Experimenting with dictionary functions!"""

__author__ = "730489697"


data: dict[str, str]

data = dict()

data = {'a': 'z', 'b': 'y', 'c': 'x'}
inverse_data = 

def inverse_dict(data):
    "The function gets a dictionary and reverses the data so that the keys become values and vice versa."
    inverse_data = {}
    for key, value in data.items