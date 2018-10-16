#!/usr/bin/python3
"""
Module contains BaseGeometry function
"""


class BaseGeometry():
    """ class BaseGeometry """

    def area(self):
        """ area function """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ checks that user entered proper value """
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))
