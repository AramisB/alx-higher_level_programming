#!/usr/bin/python3
"""
A module that defines deserialization
"""
import json


def from_json_string(my_str):
    """
    A function that deserializes a Python data structure
    argument: my_str (str) -  string to be deserialization
    Return: an object represented by a JSON string
    """
    return json.loads(my_str)
