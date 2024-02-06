#!/usr/bin/python3


def read_file(filename=""):
    """
    A function that reads a text file and prints to stdout
    Argument: filename - name of the file. Defaults to an empty string
    """
    with open(filename, encoding="utf-8") as Myfile:
        for line in Myfile:
            print(line, end="")
