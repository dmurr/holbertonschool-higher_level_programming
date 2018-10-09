#!/usr/bin/python3
"""
Module gets and sets both the width and height of a rectangle.
Contains public instance methods for area and perimeter.
"""


class Rectangle:
    """ represents a rectangle with dimensions """

    """ initializes instances """
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    """ gets width """
    @property
    def width(self):
        return self.__width

    """ sets width """
    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    """ gets height"""
    @property
    def height(self):
        return self.__height

    """ sets height"""
    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    """ returns area """
    def area(self):
        return self.width * self.height

    """ returns perimeter """
    def perimeter(self):
        if self.width == 0 or self.height == 0:
            return 0
        return self.width * 2 + self.height * 2
