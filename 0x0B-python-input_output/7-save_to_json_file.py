#!/usr/bin/python3
"""
Module contains save_to_json_file function
"""
import json


def save_to_json_file(my_obj, filename):
    """ saves object to file in json format """
    with open(filename, mode="w") as f:
        jstr = json.dumps(my_obj, f)
        f.write(jstr)
