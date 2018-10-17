#!/usr/bin/python3
"""
Module contains number_of_lines function
"""


def number_of_lines(filename=""):
    """ Returns number of lines in file"""
    nb_lines = 0
    with open(filename, encoding='UTF-8') as f:
        for line in f:
            nb_lines += 1
    return nb_lines
