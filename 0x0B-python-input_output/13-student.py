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

    def to_json(self, attrs=None):
        """ retrieves dictionary representation of student """
        if attrs is None:
            return self.__dict__
        d = {}
        for i in attrs:
            if i is "first_name":
                d[i] = self.first_name
            elif i is "last_name":
                d[i] = self.last_name
            elif i is "age":
                d[i] = self.age
        return (d)

    def reload_from_json(self, json):
        """ replaces all attributes """
        self.__dict__ = json
