#!/usr/bin/python3
"""
Module contains MyList class
"""


class MyList(list):

    def __init__(self):
        """ init method """
        pass

    def print_sorted(self):
        """ prints sorted list"""
        print(sorted(self))
