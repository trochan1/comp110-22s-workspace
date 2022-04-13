"""Utility class for numerical operations."""

from __future__ import annotations
from selectors import EpollSelector

from typing import Union

__author__ = 730489697


class Simpy:
    values: list[float]

    def __init__(self, values: list[float]):
        """Initializes the values attribute of the new object to the argument."""
        self.values = values
    
    def __str__(self) -> str:
        """Converts an object to a str representation."""
        return f"{self.values}"

    def fill(self, value: float, amount: int) -> None:
        """Fills a Simpy's values with a given number of repeating values."""
        self.values = []
        i: int = 0
        while i < amount:
            self.values.append(value)
            i += 1
    
    def arange(self, start: float, stop: float, step: float = 1.0) -> None:
        """Fills in the values for a given range of values."""
        assert step != 0.0
        self.values.append(start)
        i: float = start
        if step > 0.0:
            while i < stop - step:
                self.values.append(i + step)
                i += step
        else:
            while i + step > stop:
                self.values.append(i + step)
                i += step

    def sum(self) -> float:
        """Returns the sum or all the values."""
        result: float = sum(self.values)
        return result

    def __add__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Add method"""
        result: list[float] = []
        if isinstance(rhs, float):
            result: list[float] = []
            for value in self.values:
                result.append(value + rhs)
            return Simpy(result)
        else:
            result: list[float] = []
            for i in range(0, len(self.values)):
                result.append(self.values[i] + rhs.values[i])
            return Simpy(result)

    def __pow__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Power operator method"""
        result: list[float] = []
        if isinstance(rhs, float):
            result: list[float] = []
            for value in self.values:
                result.append(value ** rhs)
            return Simpy(result)
        else:
            result: list[float] = []
            for i in range(0, len(self.values)):
                result.append(self.values[i] ** rhs.values[i])
            return Simpy(result)

    def __eq__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """Produces a mask based on the equality of each item in the values attribute with some other Simpy object or float value."""
        result: list[bool] = []
        if isinstance(rhs, float):
            result: list[bool] = []
            for value in self.values:
                result.append(value == rhs)
            return result
        else:
            result: list[bool] = []
            for i in range(0, len(self.values)):
                result.append(self.values[i] == rhs.values[i])
            return result
        
    def __gt__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """Produces a mask based on the greater than relationship between each item in the values attribute with some other Simpy object or float value."""
        result: list[bool] = []
        if isinstance(rhs, float):
            result: list[bool] = []
            for value in self.values:
                result.append(value > rhs)
            return result
        else:
            result: list[bool] = []
            for i in range(0, len(self.values)):
                result.append(self.values[i] > rhs.values[i])
            return result

    def __getitem__(self, rhs: int) -> float:
        """Adds ability to use the subscription operator with Simpy objects."""
        i: int = 0
        for value in self.values:
            if i == rhs:
                return value
            else:
                i += 1

    def __getitem__(self, rhs: Union[int, list[bool]]) -> Union[float, Simpy]:
        """Adds ability to use the subscription operator with Simpy objects."""
        if isinstance(rhs, int):
            integer: float = 0.0
            integer = self.values[rhs]
            return integer
        else:
            result: Simpy = Simpy([])
            for i in range(0, len(self.values)):
                if rhs[i]:
                    result.values.append(self.values[i])
        return result