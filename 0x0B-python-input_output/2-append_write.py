#!/usr/bin/python3
"""
A module that defines append_write()
"""


def append_write(filename="", text=""):
    """
    A function that appends a string at the end of a file(FT8)
    Arguments: filename - the name of the file
                text (str) - the strng to append
    Return: The number of characters added
    """
    with open(filename, "a", encoding="utf-8") as myfile:
        return myfile.write(text)
