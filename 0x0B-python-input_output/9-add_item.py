#!/usr/bin/python3
"""
Module contains adds all arguments to a python list and saves to file
"""
import sys
save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file


filename = "add_item.json"
try:
    obj_list = load_from_json_file(filename)
except:
    obj_list = []

for i in range(1, len(sys.argv)):
    obj_list.append(sys.argv[i])

save_to_json_file(obj_list, filename)
