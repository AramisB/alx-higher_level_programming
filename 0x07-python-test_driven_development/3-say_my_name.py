#!/usr/bin/python3
"""
This module defines a function say_my_name
"""


def say_my_name(first_name, last_name=""):
    """
    Defines a function that prints first and second name
    variable: first_name(str) - the first name
              last_name(str) - the second name
    raises: TypeError: both names must be a string
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print(f"My name is {first_name} {last_name}")
