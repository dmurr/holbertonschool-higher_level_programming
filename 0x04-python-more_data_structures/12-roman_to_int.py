#!/usr/bin/python3
def roman_to_int(roman_string):
    answer = 0
    rom = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    if roman_string is None:
        return 0

    for i in list(roman_string):
        for k, v in rom.items():
            if i == k:
                answer += v
    return answer
