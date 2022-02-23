#!/usr/bin/env python3

# Practice using Python decorator functions
# A decorator is a function that takes another function as a parameter and can change or extend its behavior without changing the original function.




def do_twice(func):
    def wrapper(*args, **kwargs):
        func(*args, *kwargs)       
        return func(*args, *kwargs)
    return wrapper


def reverser(func):
    def wrapper(*args, **kwargs):
        word = func(*args, **kwargs)
        word = word[::-1]
        print(word)
        return word
    return wrapper


def caps(func):
    def wrapper(*args, **kwargs):
        cap = func(*args, **kwargs).upper()
        return cap
    return wrapper


@do_twice
@reverser
@caps
def name(first, last):
    fullname = first + " " + last
    print(fullname)
    return fullname


@do_twice
def last_first(name):

    name = name.split()
    name.reverse()
    name = " ".join(name)
    print(name)
    return name



if __name__ == "__main__":

    name("George", "Clooney")
    last_first("George Clooney")



