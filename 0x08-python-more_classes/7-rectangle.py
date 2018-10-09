#!/usr/bin/python3
"""
Module gets and sets both the width and height of a rectangle.
Contains public instance methods for area and perimeter.
"""


class Rectangle:
    """ represents a rectangle """

    number_of_instances = 0
    print_symbol = '#'

    """ initializes instances """
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    """ displays rectangle with str """
    def __str__(self):
        s = ""
        if self.width is 0 or self.height is 0:
            return s
        for i in range(self.height):
            s += str(self.print_symbol) * self.width
            if i is not self.height - 1:
                s += '\n'
        return s

    """ representation """
    def __repr__(self):
        return "Rectangle({},{})".format(self.width, self.height)

    """ detects when instance is deleted and prints message"""
    def __del__(self):
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

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

    """ gets height """
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
