#!/usr/bin/python3
"""
Module contains lookup function
"""


def lookup(obj):
    """
    returns the list of available attributes and methods of an object
    """
    return obj.__dir__
