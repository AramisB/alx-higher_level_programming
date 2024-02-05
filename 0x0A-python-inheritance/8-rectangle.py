#!/usr/bin/python3
"""
A module for class Rectangle
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
