#!/usr/bin/env python3


# Example of list comprehension logic
def listc():

    l = [x * y for x in range(3) for y in range(3) if x > y]

    for x in range(3):
        for y in range(3):
            if x > y:
                q = x * y
                print(q)

    return l

print(listc())


# Print all the numbers between 1 and 1000 that are divisible by 7
def listc1():

    num = [i for i in range(1, 1001) if i % 7 == 0]

    return num

print(listc1())


# Print all the numbers between 1 and 1000 that have a 3 in them
def listc2():

    num = [i for i in range(1, 1001) if "3" in str(i)]

    return num

print(listc2())


#Count the number of spaces in a string
def listc3():

    sentence = "Good night room, good night moon, good night cow jumping over the moon."
    spaces = [l for l in sentence if l == " "]

    return len(spaces)

print(listc3())


# Create a list of all the consonants in the string “Yellow Yaks like yelling and yawning and yesturday they yodled while eating yuky yams”
def listc4():

    sentence = "Yellow Yaks like yelling and yawning and yesturday they yodled while eating yuky yams"
    cons = [l for l in sentence if l not in ["a", "e", "i", "o", "u", " "]]
    
    return cons

print(listc4())


# Get the index and the value as a tuple for items in the list “hi”, 4, 8.99, ‘apple’, (‘t,b’,’n’). Result would look like (index, value), (index, value)
def listc5():

    box = ["hi", 4, 8.99, 'apple', ('t,b', 'n')]
    ugly_tuple = [(box.index(i), i) for i in box]
    return ugly_tuple

print(listc5())


# Find the common numbers in two lists (without using a tuple or set) list_a = 1, 2, 3, 4, list_b = 2, 3, 4, 5
def listc6():

    list_a = [1, 2, 3, 4]
    list_b = [2, 3, 4, 5]

    common = [num for num in list_a if num in list_b]

    return common

print(listc6())


# Get only the numbers in a sentence like ‘In 1984 there were 13 instances of a protest with over 1000 people attending’
def listc7():

    sentence = "In 1984 there were 13 instances of a protest with over 1000 people attending"
    nums = [n for n in sentence.split() if n.isdigit()]

    return nums

print(listc7())


# Given numbers = range(20), produce a list containing the word ‘even’ if a number in the numbers is even, and the word ‘odd’ if the number is odd. Result would look like ‘odd’,’odd’, ‘even’
def listc8():

    odd_even = ["even" if i % 2 == 0 else "odd" for i in range(20)]

    return odd_even

print(listc8())


# Produce a list of tuples consisting of only the matching numbers in these lists list_a = 1, 2, 3,4,5,6,7,8,9, list_b = 2, 7, 1, 12. Result would look like (4,4), (12,12)
def listc9():

    list_a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    list_b = [2, 7, 1 , 12]

    matches = [(x, x) for x in list_a if x in list_b]
    return matches

print(listc9())


# Find all of the words in a string that are less than 4 letters
def listc10():

    sentence = "He told me that the man of my dreams would be just out of reach, betrothed to another"
    lll = [word for word in sentence.split() if len(word) < 4]

    return lll

print(listc10())


# Use a nested list comprehension to find all of the numbers from 1-1000 that are divisible by any single digit besides 1 (2-9)
def listc11():

    nums = [num for num in range(1, 1001) if True in [True for div in range(2, 10) if num % div == 0]]

    return nums

print(listc11())