#!/usr/bin/python3
Rectangle = __import__('9-rectangle').Rectangle
"""
Module contains subclass of Rectangle, Square
"""


class Square(Rectangle):
    """ Square class """

    def __init__(self, size):
        """ initializes square with positive size """
        self.__size = size
        self.integer_validator("size", size)

    def __str__(self):
        """ string representation of object """
        return "[{}] {:d}/{:d}".format(self.__class__.__name__,
                                       self.__size, self.__size)

    def area(self):
        return self.__size * self.__size
