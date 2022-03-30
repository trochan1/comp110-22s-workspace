"""Dictionary related utility functions."""

__author__ = "730489697"


def read_csv_rows(nc_durham_2015_march_21_to_26.csv: str) -> list[dict[str, str]]:
    """Reads the rows of a csv into a 'table'."""
    result: list[dict[str, str]] = []

    file_handle = open(nc_durham_2015_march_21_to_26.csv, "r", encoding="utf8")

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

    first_row: dict[str, str] = rowtable[0]
    for column in first_row:
        result[column] = column_values(row_table, column)

    return result


def head(data_cols_head: dict[str, list[str]], n: int) -> dict[str, list[str]]:
    """Produces a new column-based table with only the first N rows of data."""
    result: dict[str, list[str]] = {}
    if n > len(data_cols_head):
        n = len(data_cols_head)
    for column in data_cols_head:
        lst: list[str] = []
        for i in range(0, n):
            lst.append(data_cols_head[column][i])
            i += 1
        result[column] = lst
    return result


def select(data_cols_head: dict[str, list[str]], nm: list[str]) -> dict[str, list[str]]:
    """Produces a new column based table with a subset of the original columns."""
    result: dict[str, list[str]] = {}
    for column in nm:
        result[column] = data_cols_head[column]
    return result


def concat(data_cols_head: dict[str, list[str]], new_table: dict[str, list[str]]) -> dict[str, list[str]]:
    """Produces a new column-based table with two column based tables."""
    result: dict[str, list[str]] = {}
    for column in data_cols_head:
        result[column] = data_cols_head[column]
    for a in new_table:
        if a in result:
            for i in new_table:
                result[a].append(i)
            else:
                result[a].append(i)
        return result


def count(lst: list[str]) -> dict[str, int]:
    """Produces a dict where every key is a unique value in a list."""
    lt: dict[str, int] = {}
    for i in lt:
        if i in lt:
            lt[i] += 1
        else:
            lt[i] = 1

    return lt