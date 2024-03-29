#!/usr/bin/python3
"""
A module is_same_class
"""


def is_same_class(obj, a_class):
    """
    Defines a function that return true if the object
    is exactly an instance of the specified class: otherwise False.
    """
    return type(obj) == a_class
