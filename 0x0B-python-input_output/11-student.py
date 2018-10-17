#!/usr/bin/python3
"""
Module contains Student class
"""


class Student:
    """ student class"""

    def __init__(self, first_name, last_name, age):
        """ initializes class """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ dictionary rep of attributes"""
        return self.__dict__
