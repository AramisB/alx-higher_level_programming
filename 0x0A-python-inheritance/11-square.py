#!/usr/bin/python3
"""
A module for class BaseGeometry
"""


class BaseGeometry:
    """
    A class that defines geometry
    """

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
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """
        A public instance that calculates the area
        Raises: Exception
        """
        return (self.__width * self.__height)

    def __str__(self):
        """
        Returns a string representation of a rectangle
        """
        return f"[Rectangle] {self.__width} / {self.__height}"

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
        self.__size = size

    def area(self):
        """
        Calculates the area of a square
        """
        return (self.__size ** 2)

    def __str__(self):
        """
        Returns a string representation of a rectangle
        """
        return f"[Square] {self.__width} / {self.__height}"
