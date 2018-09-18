#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix is None:
        return None

    for row in matrix:
        pos = 0
        for i in row:
            if pos == len(row) - 1:
                print("{:d}".format(i), end="")
            else:
                print("{:d}".format(i), end=" ")
            pos += 1
        print()
