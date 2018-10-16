#!/usr/bin/python3
"""
Module contains inherits_from function
"""


def inherits_from(obj, a_class):
    """ checks if object is a direct or indirect instance of a_class """
    if issubclass(type(obj), a_class) and a_class != type(obj):
        return True
    else:
        return False
