#!/usr/bin/env python3


"""
Description:
Write a function, persistence, that takes in a positive parameter num and returns its multiplicative persistence, which is the number of times you must multiply the digits in num until you reach a single digit.
"""


def persistence(num):

    numlist = [i for i in str(num)]
    count = 0

    while len(numlist) > 1:
        result = 1

        for num in numlist:
            result = result * int(num)

        count += 1
        numlist = [i for i in str(result)]

    return count

if __name__ == "__main__":

    print(persistence(999))