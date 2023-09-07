#!/usr/bin/python3
# This script is designed for unit tests on the max_integer function.

import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    # Define unit tests for the max_integer function.

    def test_ordered_list(self):
        # Testing the function with an ordered list of integers.
        ordered = [1, 2, 3, 4]
        self.assertEqual(max_integer(ordered), 4)

    def test_unordered_list(self):
        # Testing the function with an unordered list of integers.
        unordered = [1, 2, 4, 3]
        self.assertEqual(max_integer(unordered), 4)

    def test_max_at_beginning(self):
        # Testing the function with a list where the maximum value is at the beginning.
        max_at_beginning = [4, 3, 2, 1]
        self.assertEqual(max_integer(max_at_beginning), 4)

    def test_empty_list(self):
        # Testing the function with an empty list.
        empty = []
        self.assertEqual(max_integer(empty), None)

    def test_one_element_list(self):
        # Testing the function with a list containing a single element.
        one_element = [7]
        self.assertEqual(max_integer(one_element), 7)

    def test_floats(self):
        # Testing the function with a list of floating-point numbers.
        floats = [1.53, 6.33, -9.123, 15.2, 6.0]
        self.assertEqual(max_integer(floats), 15.2)

    def test_ints_and_floats(self):
        # Testing the function with a list containing both integers and floats.
        ints_and_floats = [1.53, 15.5, -9, 15, 6]
        self.assertEqual(max_integer(ints_and_floats), 15.5)

    def test_string(self):
        # Testing the function with a string input.
        string = "Brennan"
        self.assertEqual(max_integer(string), 'r')

    def test_list_of_strings(self):
        # Testing the function with a list of strings.
        strings = ["Brennan", "is", "my", "name"]
        self.assertEqual(max_integer(strings), "name")

    def test_empty_string(self):
        # Testing the function with an empty string.
        self.assertEqual(max_integer(""), None)

if __name__ == '__main__':
    unittest.main()
