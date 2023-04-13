#!/usr/bin/python3
"""The module that defines the to_json_string function"""


import json


def from_json_string(my_str):
    """Returns the JSON repr of an object (string)
    Args:
    my_obj (str): object to return JSON repr of
    """
    return json.loads(my_str)
