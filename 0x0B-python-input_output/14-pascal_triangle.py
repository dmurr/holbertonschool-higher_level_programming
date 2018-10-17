#!/usr/bin/python3
"""
Module contains function pascal_triangle
"""


def pascal_triangle(n):
    """ created a pascal triangle """
    if n <= 0:
        return []

    pascal = [[1]]
    for i, row in enumerate(pascal):
        temp_list = []
        for j, num in enumerate(row):
            if j < len(row) - 1:
                temp_list.append(row[j] + row[j+1])
        ready = []
        ready.append(1)
        if len(temp_list) > 0:
            for k in temp_list:
                ready.append(k)
        ready.append(1)
        pascal.append(ready)

        if i == (n - 1):
            return pascal
