#!/usr/bin/env python3

# Practice using Python Generator functions
# A Generator function provides a simple way of creating an iterator in Python. It is built by defining a regular function with at least 1 YIELD statement. The yield statement pauses the function, and continues at the same point if/when the function is called again.



def get_info():

    name = "George Clooney"
    job = "Actor"
    age = 55
    location = "Los Angeles, CA"

    yield name
    yield job
    yield age
    yield location



def poem():

    yield "Roses are red"
    yield "Violets are blue"
    yield "I forgot the words"
    yield "and so did you."



if __name__ == "__main__":

    info = get_info()
    print(next(info))
    print(next(info))
    print(next(info))
    print(next(info))
    print(next(info))

    for item in poem():
        print(item)