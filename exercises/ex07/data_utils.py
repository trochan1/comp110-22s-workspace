"""Dictionary related utility functions."""

__author__ = "730489697"

from csv import DictReader


def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Reads the rows of a csv into a 'table'."""
    result: list[dict[str, str]] = []
    file_handle = open(filename, "r", encoding="utf8")
    csv_reader = DictReader(file_handle)
    for row in csv_reader:
        result.append(row)
    file_handle.close()
    return result


def column_values(table: list[dict[str, str]], column: str) -> list[str]:
    """Produces a list[str[ of all values in a single column."""
    result: list[str] = []
    for row in table:
        item: str = row[column]
        result.append(item)
    return result


def columnar(row_table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Transforms a row-oriented table to a column-oriented table."""
    result: dict[str, list[str]] = {}
    first_row: dict[str, str] = row_table[0]
    for column in first_row:
        result[column] = column_values(row_table, column)
    return result


def head(x: dict[str, list[str]], y: int) -> dict[str, list[str]]:
    """Produces a new column-based table with only the first N rows of data."""
    result: dict[str, list[str]] = {}
    if y > len(x):
        y = len(x)
    for column in x:
        lst: list[str] = []
        i: int = 0
        while i < y:
            lst.append(x[column][i])
            i += 1
        result[column] = lst
    return result


def select(x: dict[str, list[str]], nm: list[str]) -> dict[str, list[str]]:
    """Produces a new column based table with a subset of the original columns."""
    result: dict[str, list[str]] = {}
    for column in nm:
        result[column] = x[column]
    return result


def concat(x: dict[str, list[str]], y: dict[str, list[str]]) -> dict[str, list[str]]:
    """Produces a new column-based table with two column based tables."""
    result: dict[str, list[str]] = {}
    for column in x:
        result[column] = x[column]
    for a in y:
        if a in result:
            result[a] = result[a] + y[a]
        else:
            result[a] = y[a]
    return result


def count(lst: list[str]) -> dict[str, int]:
    """Produces a dict where every key is a unique value in a list."""
    lt: dict[str, int] = {}
    for i in lst:
        if i in lt:
            lt[i] += 1
        else:
            lt[i] = 1

    return lt