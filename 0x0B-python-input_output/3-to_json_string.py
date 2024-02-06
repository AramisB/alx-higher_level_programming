#!/usr/bin/python3
"""
A module that defines a JSON representation function
"""

import json


def to_json_string(my_obj):
    """
    A function that converts data into string representation(serializing)
    Arguments: my_obj - the data
    Return: string representation of the data
    """
    return json.dumps(my_obj)
