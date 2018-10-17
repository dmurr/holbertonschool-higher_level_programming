#!/usr/bin/python3
"""
Module contains load_from_json_file
"""
import json


def load_from_json_file(filename):
    """ creates object from json file """
    with open(filename) as f:
        return json.load(f)
