#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry
"""
Module contains Rectangle class
"""


class Rectangle(BaseGeometry):
    """ class Rectangle """

    def __init__(self, width, height):
        """ initialize Rectangle and check values """
        self.__width = width
        self.__height = height
        self.integer_validator("width", self.__width)
        self.integer_validator("height", self.__height)
