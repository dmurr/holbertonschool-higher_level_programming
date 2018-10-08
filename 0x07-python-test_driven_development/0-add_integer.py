#!/usr/bin/python3
"""
This module contains an addition function.
"""


def add_integer(a, b=98):
    """ Addition Function """

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")

    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    if a != a or b != b:
        raise ValueError("unsupported type")

    result = a + b
    if result == float('inf') or result == float('inf'):
        raise ValueError("Error")

    return int(a) + int(b)
