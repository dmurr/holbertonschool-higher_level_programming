#!/usr/bin/python3
"""
Module contains text_indentation function



"""
def text_indentation(text):
    """ prints text with two newlines after each '.', '?',':' """

    if text is None:
        raise TypeError("text must be a string")

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    my_list = list(text)

    for i, v in enumerate(my_list):
        if v is '.' or v is '?' or v is ':':
            my_list[i] = '\n'
            my_list[i+1] = '\n'

    print("".join(my_list))
