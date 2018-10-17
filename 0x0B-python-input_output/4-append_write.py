#!/usr/bin/python3
"""
Module contains append_write function
"""
write_file = __import__('3-write_file').write_file


def append_write(filename="", text=""):
    """ appends text and return number of appended characters """
    try:
        with open(filename, mode="a", encoding="UTF-8") as f:
            f.write(text)
        return len(text)
    except:
        write_file(filename)
