#!/usr/bin/python3
def no_c(my_string):
    new_str = list(my_string)
    for i, v in enumerate(new_str):
        if v is 'C' or v is 'c':
            del new_str[i]
    return "".join(new_str)
