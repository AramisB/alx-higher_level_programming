#!/usr/bin/python3
"""
A module that creates a class MyInt
"""


class MyInt(int):
    """
    A class that inherits from int.
    It's a rebel that inverts == and != opertors
    """
    def __eq__(self, value):
        """
        Overrides == opeartor with !=
        """
        return self.real != value

    def __ne__(self, value):
        """
        Overrides != operator with ==
        """
        return self.real == value
