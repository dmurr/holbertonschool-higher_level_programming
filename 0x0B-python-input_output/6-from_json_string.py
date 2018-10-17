#!/usr/bin/python3
"""
Module contains from_json_string function
"""
import json


def from_json_string(my_str):
    """ converts json string to object"""
    return json.loads(my_str)
