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
        """save_to_file: writes the json string
        representation of list_objs to a file
        Args:
            cls: the class
            list_objs: a list of instances
        """
        f = "{}.json".format(cls.__name__)
        with open(f, mode="w", encoding='utf-8') as wtf:
            if list_objs is None:
                wtf.write("[]")
            else:
                j = []
                for i in list_objs:
                    j.append(i.to_dictionary())
                wtf.write(cls.to_json_string(j))

    @staticmethod
    def from_json_string(json_string):
        """from_json_string: deserialize json string
        Args:
            json_string: a string representing a list of dictionaries
        Return:
            returns the list of the json string representation json_string
        """
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """create classmethod: Dictionary to Instance
        Args:
        cls: the class
        dictionary: double pointer to a dictionary
        Return: an instance with attributes set
        """
        if cls.__name__ == "Rectangle":
            new = cls(1, 1)
        if cls.__name__ == "Square":
            new = cls(1)
        new.update(**dictionary)
        return new

    @classmethod
    def load_from_file(cls):
        """load_from_file: File to instances
        Args:
           cls: the class
        Return:
           returns a list of instances
        """
        filename = "{}.json".format(cls.__name__)
        list_instance = []
        try:
            with open(filename, mode="r", encoding='utf-8') as f:
                list_dict = cls.from_json_string(f.read())
            for d in list_dict:
                list_instance.append(cls.create(**d))
            return list_instance
        except FileNotFoundError:
            return []
