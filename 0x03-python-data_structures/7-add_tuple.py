#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) is 0 and len(tuple_b) is 0:
        return None

    if len(tuple_a) is 0:
        i = tuple_b[0]
        j = tuple_b[1]
    elif len(tuple_b) is 0:
        i = tuple_a[0]
        j = tuple_a[1]
    elif len(tuple_a) is 1 :
        i = tuple_a[0]
        j = tuple_a[1] + tuple_b[1]
    elif len(tuple_b) is 1 :
        i = tuple_a[0] + tuple_b[0]
        j = tuple_a[1]
    else:
        i = tuple_a[0] + tuple_b[0]
        j = tuple_a[1] + tuple_b[1]
    return (i,j)
