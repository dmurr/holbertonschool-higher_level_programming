#!/usr/bin/python3
def weight_average(my_list=[]):
    dividend = 0
    divisor = 0

    if my_list is None:
        return 0

    for x, y in my_list:
        dividend += x * y
        divisor += y
    return dividend / divisor
