#!/usr/bin/python3
"""
A module that defines class square
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    A class that inherits from Rectangle
    """
    def __init__(self, size):
        """
        Instatiates the square
        args: size (int) - size of the square
        raises: ValueError - size must be > 0
                TypeError - size must be an integer
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
