#!/usr/bin/python3
"""
A module that adds two integers
"""


def add_integer(a, b=98):
    """
    Defines a function that adds two integers
    argument: a is the first argument
               b is the second argument
    Raises: TypeError: arguments must be integers or floats
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    """
    Float arguments are typecasted to ints before addition is performed.
    """
    return int(a) + int(b)
