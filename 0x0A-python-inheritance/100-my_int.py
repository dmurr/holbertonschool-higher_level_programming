#!/usr/bin/python3
"""
Module contains class MyInt
"""


class MyInt(int):
    """ class MyInt """

    def __init__(self, value):
        """ initialized MyInt """
        self.value = value

    def __eq__(self, other):
        """ NOTequals  """
        return self.value != other

    def __ne__(self, other):
        """ equals """
        return self.value == other
