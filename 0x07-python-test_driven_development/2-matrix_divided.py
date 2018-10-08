#!/usr/bin/python3
"""
Module contains matrix_dividend function
"""


def matrix_divided(matrix, div):
    """
    Divide Matrix
    """
    list_lengths = []

    if div == 0:
        raise ZeroDivisionError("division by zero")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    for row in matrix:
        list_lengths.append(len(row))
        if len(set(list_lengths)) != 1:
            raise TypeError("Each row of the matrix must have the same size")
        for i in row:
            if not isinstance(i, (int, float)):
                raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats")

    return [[round(i / div, 2) for i in row] for row in matrix]
