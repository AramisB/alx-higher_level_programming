#!/usr/bin/python3
"""
This module defines a class Rectangle
"""


class Rectangle:
    """
    Defines a rectangle
    """
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """
        Initializes the dimensions of a rectangle
        args: width (int) - width of the rectangle
              height (int) - height of the rectangle
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """
        retrieves the width of the rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        sets width to value
        args: value (int) - new width
        raises: ValueError - value must be > 0
                TypeError - value must be an int
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Retrieves the height of the rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Sets heigh to value
        args: value (int) - the new height
        raises: TypeError - height must be an integer
                ValuError - height must be >= 0
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        calculates the area of the triangle
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        calculates the perimeter of the rectangle
        if width or height is 0, perimeter is 0
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width * 2) + (self.__height * 2)

    def __str__(self):
        """
        Returns a string representation of the rectangle
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        str_rectangle = ""
        for _ in range(self.__height):
            str_rectangle += str(self.print_symbol) * self.__width + "\n"
        return str_rectangle.rstrip()

    def __repr__(self):
        """
        Returns a string representation
        that can be used to recreate the rectangle
        """
        return (f"Rectangle({self.__width}, {self.height})")

    def __del__(self):
        """
        Deletes the instance of a rectangle
        """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        Returns the biggest rectangle based on the area
        args: rect_1 - the first rectangle
              rect_2 - the second rectangle
        raises: rect_1 and rect_2 must be instances of Rectangle
        return: rect_1 if both have the same area value
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")

        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() >= rect_2.area():
            return rect_1

    @classmethod
    def square(cls, size=0):
        """
        Returns a new rectangle instance
        arg:cls - the class
            size (int) - size of the square(equal to width and height)
        """
        return (cls(size, size))
