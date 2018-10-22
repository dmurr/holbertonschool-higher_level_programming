#!/usr/bin/python3
"""
Base class
"""
import json


class Base:
    """ Base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """ if id is given sets instance id else increase obj """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = self.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries is None or not list_dictionaries:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        with open("{}.json".format(cls.__name__), "w") as wtf:
            json.dump(cls.to_json_string(list_objs), wtf)
