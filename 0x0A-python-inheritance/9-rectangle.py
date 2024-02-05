#!/usr/bin/python3
"""
A module for class BaseGeometry
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Defines a rectangle that inherits from BaseGeometry
    """

    def __init__(self, width, height):
        """
        Instatiation of a rectangle
        args: width (int) - width of the rectangle
              height (int) - height of the rectangle
        """
        super().__init__()
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """
        return the area of a rectangle
        """
        return (self.__width * self.__height)

    def __str__(self):
        """
        Returns a string representation of a rectangle
        """
        string = "[" + str(self.__class__.__name__) + "] "
        string += str(self.__width) + "/" + str(self.__height)
        return string
