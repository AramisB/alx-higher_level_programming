#!/usr/bin/python3
"""
A module for inherits_from
"""


def inherits_from(obj, a_class):
    """
    A function that returns True if the object is an instance 
    that inherited from a specified class: False otherwise
    """
    return type(obj) is not a_class and issubclass(type(obj), a_class)
