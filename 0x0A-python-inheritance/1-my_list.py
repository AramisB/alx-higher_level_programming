#!/usr/bin/python3
"""
A module that defines class MyList
"""


class MyList(list):
    """
    A class that inherits from list
    """
    def print_sorted(self):
        """
        A public instance that prints an ascending sorted list
        """
        print(sorted(self))
