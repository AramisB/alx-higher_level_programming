#!/usr/bin/python3
"""
A module for is_kind_of_class
"""


def is_kind_of_class(obj, a_class):
    """
    Defines a function that returns true if the object is an instance of,
    or if the object is an instance of a class that inherited from,
    the specified class: False otherwise
    """
    return isinstance(obj, a_class)
