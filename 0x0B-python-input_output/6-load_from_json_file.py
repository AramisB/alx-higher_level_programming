#!/usr/bin/python3
"""
A module that defines a load_from_json_file()
"""
import json


def load_from_json_file(filename):
    """
    A function that creates an object from a JSON file
    Argument: filename - the name of the file
    """
    with open(filename) as myfile:
        return json.load(myfile)
