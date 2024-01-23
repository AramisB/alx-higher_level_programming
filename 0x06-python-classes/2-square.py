#!/usr/bin/python3
"""
This module defines a class Square
"""


class Square:
    """
    This class represents a square
    """

    def __init__(self, size=0):
        """
        Initializes a new instance of class Square
        Args:
            size (int): size of the square
        Raises:
            TypeError: if size is not an integer
            ValueError: if size is less than 0
        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer.")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
