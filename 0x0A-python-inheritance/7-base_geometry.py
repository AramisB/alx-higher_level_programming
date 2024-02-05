#!/usr/bin/python3
"""
A module for class BaseGeometry
"""


class BaseGeometry:
    """
    A class that defines geometry
    """
    pass

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
        if type(value) != int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
