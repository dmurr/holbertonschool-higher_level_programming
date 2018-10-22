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
        """ to_json_string:
        Args:

        Return:

        """
        if list_dictionaries is None or not list_dictionaries:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ save_to_file:

        Args:

        Returns:
        """
        f = "{}.json".format(cls.__name__)
        if list_objs is None or list_objs is "":
            with open(f, mode="w", encodings='utf-8') as wtf:
                wtf.write("[]")
        else:
            j = []
            for i in list_objs:
                j.append(i.to_dictionary())
            j = cls.to_json_string(j)
            with open(f, mode="w", encoding='utf-8') as wtf:
                wtf.write(j)
