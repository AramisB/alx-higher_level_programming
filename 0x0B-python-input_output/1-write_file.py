#!/usr/bin/python3
"""
A module that defines write_file()
"""


def write_file(filename="", text=""):
    """
    A function that writes to a text file (UTF8)
    Arguments: filename - name of the file
                text (str) - string to return
    Returns the number of characters written
    """
    with open(filename, "w", encoding="utf-8") as myfile:
        return myfile.write(text)
