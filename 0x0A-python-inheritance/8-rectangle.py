#!/usr/bin/python3
"""
A module for class BaseGeometry
"""


class BaseGeometry:
    """
    A class that defines geometry
    """
    
    def area(self):
        """
        A public instance
        Raises: Exception
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        a public isntace that validates value
        Raises: TypeError - if value is not an integer
                ValueError - if value <= 0
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")

class Rectangle(BaseGeometry):
    """
    Defines a rectangle
    """
    
    def __init__(self, width, height):
        """
        Instatiation of a rectangle
        args: width (int) - width of the rectangle
              height (int) - height of the rectangle
        """
        super().__init__()
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
