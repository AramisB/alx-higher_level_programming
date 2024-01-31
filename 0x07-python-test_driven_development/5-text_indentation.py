#!/usr/bin/python3
"""
This module defines a function for text indentation
"""


def text_indentation(text):
    """
    A function that prints a text with 2 new lines after ., ? or :
    Args: text (str) - the text to print
    Raises: TypeError: if text is not a string
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    index = 0

    while index < len(text) and text[index] == ' ':
        index += 1
    while index < len(text):
        print(text[index], end="")
        if text[index] == "\n" or text[index] in ".?:":
            if text[index] in ".?:":
                print("\n")
            index += 1
            while index < len(text) and text[index] == ' ':
                index += 1
            continue
        index += 1
