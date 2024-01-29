#!/usr/bin/python3
"""
This module defines a class Rectangle
"""


class Rectangle:
    """
    A class for a rectangle
    """
    def __init__(self, width=0, height=0):
        """
        Initializes the dimensions of the rectangle
        args: width (int) - the width
              height (int) - the height
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
        sets width to value
        args: value (int) - the new width
        raises: TypeError - width must be an integer
                ValueError - width must be >= 0
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        
        if value < 0:
            raise ValueError("width must be >= 0")
        
        self.__width = value

    @property
    def height(self):
        """
        Retrieves height of the rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        sets height to value
        args: value - new height of the rectangle
        raises: TypeError - height must be an integer
                ValueError - height must be >= 0
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        
        if value < 0:
            raise ValueError("height must be >= 0")
        
        self.__height = value

    def area(self):
        """
        calculates the area of a rectangle
        """
        return (self.__width * self.__height)

    def perimeter(self):
        """
        calculates the perimeter of the rectangle
        """
        if self.__width == 0 or self.__height == 0:
            perimeter == 0
        
        return (self.__width * 2) + (self.__height * 2)
