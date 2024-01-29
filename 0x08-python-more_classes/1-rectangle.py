#!/usr/bin/python3
"""
This module defines a class Rectangle
"""


class Rectangle:
    """
    Defines a rectangle
    """
    def __init__(self, width=0, height=0):
        """
        Initializes the dimensions of a rectangle
        args: width (int) - width of the rectangle
              height (int) - height of the rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Retrieves the width of the rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Sets width to value
        args: value (int) - the new width
        Raises: TypeError - value should be an integer
                ValueError - value should be >= 0
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")

        if value < 0:
            raise ValueError("width must be >=0")

        self.__width = value

    @property
    def height(self):
        """
        Retrieves ths height of the rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Sets with to value
        args: value (int) - the new height
        raises: ValueError - value must be >= 0
                TypeError - value must be an integer
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")

        if value < 0:
            raise ValueError("Height must be >= 0")

        self.__height = value
