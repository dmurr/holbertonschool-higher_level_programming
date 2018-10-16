#!/usr/bin/python3
"""
Module contains add_attribute function
"""


def add_attribute(obj, name, val):
    """ adds attribute if it can """

    if hasattr(obj, "__dict__") is False:
        raise TypeError("can't add new attribute")
    else:
        setattr(obj, name, val)
