#!/usr/bin/python3
"""
Module contains print_square function
"""


def print_square(size):
    """ print_square function """

    if isinstance(size, float) and size < 0.0:
        raise TypeError("size must be an integer")
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        for n, j in enumerate(range(size)):
            if n < size - 1:
                print("#", end="")
            else:
                print("#")
