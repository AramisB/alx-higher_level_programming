#!/usr/bin/python3
"""
A module that defines a save_to_json_file()
"""
import json


def save_to_json_file(my_obj, filename):
    """
    A function that writes an object to a text file using JSON representation
    Argument: my_obj - the object
                filename - name of the file
    """
    with open(filename, "w") as myfile:
        return json.dump(my_obj, myfile)
