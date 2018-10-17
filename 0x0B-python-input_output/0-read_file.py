#!/usr/bin/python3
"""
Module contains read_file function
"""


def read_file(filename=""):
    """ opens stream, reads file, and closes stream """
    with open(filename, encoding='UTF-8') as f:
        for line in f:
            print(line, end="")
