#!/usr/bin/python3
"""
Module contains write_file function
"""


def write_file(filename="", text=""):
    """ writes text to a file and return characters written """
    with open(filename, mode="w", encoding="UTF-8") as f:
        f.write(text)
    return len(text)
