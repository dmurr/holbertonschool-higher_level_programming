#!/usr/bin/python3
"""
Module contains function is_same_class
"""


def is_same_class(obj, a_class):
    """ checks if object is the exact same class """
    if type(obj) is a_class:
        return True
    else:
        return False
