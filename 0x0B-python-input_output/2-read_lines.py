#!/usr/bin/python3
"""
Module contains read_lines function
"""
read_file = __import__('0-read_file').read_file
number_of_lines = __import__('1-number_of_lines').number_of_lines


def read_lines(filename="", nb_lines=0):
    """ displays specified number of lines of file """
    total_lines = number_of_lines(filename)
    if nb_lines <= 0 or nb_lines >= total_lines:
        read_file(filename)
    else:
        with open(filename, encoding="UTF-8") as f:
            for i, line in enumerate(f):
                if i < nb_lines:
                    print(line, end="")
