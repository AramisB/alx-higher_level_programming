#!/usr/bin/python3
"""
This module defines a class Square
"""


class Square:
    """
    Represent a square
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initialize a new square
        Args:
            size (int): The size of the new square
            position (int, int): The position of the new square
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """
        Get the current size of the square
        """
        return (self.__size)

    @size.setter
    def size(self, value):
        """
        sets the current size of the square
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """
        Get the current position of the square
        """
        return (self.__position)

    @position.setter
    def position(self, value):
        """
        sets the current position of the square
        """
        if type(value) is not tuple or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not all(isinstance(num, int) and num >= 0 for num in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
        Return the current area of the square
        """
        return self.__size ** 2

    def my_print(self):
        """
        Print the square with the # character
        """
        if self.__size == 0:
            print()
        else:
            for i in range(self.__position[1]):
                print()
            for i in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
