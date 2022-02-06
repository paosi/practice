#!/usr/bin/env python3

import unittest
import fizzbuzz


class Test(unittest.TestCase):

    def test3(self):
        self.assertEqual(fizzbuzz.fizzbuzz(6), "Fizz")

    def test5(self):
        self.assertEqual(fizzbuzz.fizzbuzz(10), "Buzz")

    def testfb(self):
        self.assertEqual(fizzbuzz.fizzbuzz(30), "FizzBuzz")

    def testnum(self):
        self.assertEqual(fizzbuzz.fizzbuzz(2), 2)
        self.assertEqual(fizzbuzz.fizzbuzz(98), 98)



if __name__ == "__main__":

    unittest.main()