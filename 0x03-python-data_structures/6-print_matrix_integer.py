#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix is None:
        return None

    for row in matrix:
        for i, v in enumerate(row):
            if i == len(row) - 1:
                print("{:d}".format(v), end="")
            else:
                print("{:d}".format(v), end=" ")
        print()
