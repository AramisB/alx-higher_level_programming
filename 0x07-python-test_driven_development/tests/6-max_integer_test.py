#!/usr/bin/python3
"""
Unittest for max_integer([..])
"""



import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """
    defines the test cases for max_integer
    """
    def test_ordered_list(self):
        """
        Tests for an ordered list of integers
        """
        ordered = [1, 2, 3, 4, 5]
        self.assertEqual(max_integer(ordered), 5)

    def test_unordered_list(self):
        """
        Tests for unordered list of integers
        """
        unordered = [17, 23, 9, 18, 3]
        self.assertEqual(max_integer(unordered), 23)

    def test_max_at_beginning(self):
        """
        Test when there is a maximum value at the beginning
        """
        max_at_beginning = [101, 67, 89, 5, 40]
        self.assertEqual(max_integer(max_at_beginning), 101)

    def test_empty_list(self):
        """
        Tests an empty list
        """
        empty_list = []
        self.assertEqual(max_integer(empty_list), None)
     
    def test_float_list(self):
        """
        Tests a list containing floats
        """
        float_list = [4.5, 90.32, 75.0, 67.34, 187.5]
        self.assertEqual(max_integer(float_list), 187.5)

    def test_one_element(self):
        """
        Test when only one element is in a list
        """
        one_element = [31]
        self.assertEqual(max_integer(one_element), 31)

    def test_ints_floats(self):
        """
        Tests when a list has both integers and floats
        """
        ints_floats = [23, 76.9, 6, 90.3, 26.7]
        self.assertEqual(max_integer(ints_floats), 90.3)

    def test_string(self):
        """
        Tests a list with a string
        """
        string = "Aramis"
        self.assertEqual(max_integer(string), 's')

    def test_list_strings(self):
        """
        Tests a list of string for maximum value
        """
        list_strings = ["I", "am", "the", "best", "at", "coding"]
        self.assertEqual(max_integer(list_strings), 'the')

    def test_empty_string(self):
        """
        Tests an empty string
        """
        self.assertEqual(max_integer(""), None)
