#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    isNegative = True
else:
    isNegative = False
if isNegative:
    temp = -number
    lastDigit = 0 - temp % 10
else:
    lastDigit = number % 10
print("Last digit of {:d} is {:d} ".format(number, lastDigit), end='')
if lastDigit > 5:
    print("and is greater than 5")
elif lastDigit == 0:
    print("and is 0")
elif lastDigit < 6:
    print("and is less than 6 and not 0")
