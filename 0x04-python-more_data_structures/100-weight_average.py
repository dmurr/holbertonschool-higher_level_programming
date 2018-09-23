#!/usr/bin/python3
def weight_average(my_list=[]):
    dividend = 0
    divisor = 0

    if len(my_list) is 0:
        return 0

    for x, y in my_list:
        dividend += x * y
        divisor += y
    return dividend / divisor
