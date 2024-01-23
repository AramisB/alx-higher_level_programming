#!/usr/bin/python3
"""
This module defines the Square class
"""


class Square:
    """
    This class represents a square
    """
    def __init__(self, size=0):
        """
        Initilizes a new instance for the Square class
        args: size - size of the square
        """
        self.__size = size

    @property
    def size(self):
        """
        retrives the  size of a square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        sets size to value
        arg: value - the new size of the square
        raises:ValueError - size must be greater than 0
               TypeError - size must be of type int
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be greater than 0")
        self.__size = value

    def area(self):
        """
        calculates the area of the square
        """
        return self.__size ** 2
