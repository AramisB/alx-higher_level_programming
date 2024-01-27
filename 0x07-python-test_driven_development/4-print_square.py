#!/usr/bin/python3
"""
A module that defines a function to print a square
"""


def print_square(size):
    """
    A function that prints a square
    variable: size - the size length of a square
    Raises: TypeError - size must be an integer
            ValueError - size must be greater than 0
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >=0")
    for i in range(size):
        for j in range(size):
            print("#", end="")
        print("")
