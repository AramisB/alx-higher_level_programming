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
        This initializes a new instance of class Square
        Args: Size - size of the square
        """

        if type(size) is not int:
            """
            This is a TypeError exception
            """

            raise TypeError("Size must be an integer.")
        if size < 0:
            """
            This is a ValueError exception
            """

            raise ValueError("Size must be >= 0")
        self.__size = size
