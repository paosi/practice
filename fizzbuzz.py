#!/usr/bin/env python3


def fizzbuzz(i):

    if i % 3 == 0 and i % 5 == 0:
        return "FizzBuzz"

    elif i % 3 == 0:
        return "Fizz"

    elif i % 5 == 0:
        return "Buzz"

    else:
        return i


if __name__ == "__main__":

    i = 1
    while i <= 100:
        print(fizzbuzz(i))
        i += 1
            

