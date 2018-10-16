#!/usr/bin/python3
"""
Module contains is_kind_of_class function
"""


def is_kind_of_class(obj, a_class):
    """ checks if object is an instance of a_class """
    if isinstance(obj, a_class):
        return True
    else:
        return False
