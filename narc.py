#!/usr/bin/env python3

from string import digits


"""
Return True if a given number is 'narcississtic'. A narcississtic number is one where the sum of the individual digits
raised to the power of the number of digits in the number equals the original number. Ex. 3^3 + 7^3 + 1^3 = 371, so 371
is a narcissistic number.
"""


def narcissistic(value):
    
    if value in range(0,10):
        return True
    elif value >= 10:
        str_value = str(value)
        total = 0
        for digit in str_value:
            expo = int(digit) ** len(str_value)
            total = total + expo
        if total == value:
            return True
        else:
            return False



if __name__ == "__main__":

    print(narcissistic(7))
    print(narcissistic(371))
    print(narcissistic(122))
    print(narcissistic(4887))