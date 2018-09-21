#!/usr/bin/python3
def roman_to_int(roman_string):
    total = 0
    r = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    if roman_string is None or type(roman_string) is not str:
        return 0

    temp = []
    for letter in list(roman_string):
        for k, v in r.items():
            if letter == k:
                temp.append(v)

    for i, x in enumerate(temp):
        if i == len(temp) - 1:
            total += x
        elif x >= temp[i + 1]:
            total += x
        else:
            total -= x

    return total
