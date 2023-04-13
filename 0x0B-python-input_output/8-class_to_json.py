#!/usr/bin/python3
"""The module that creates a function  that returns the dict for JSON"""


def class_to_json(obj):
    """Returns the dictionary description of object
    Args:
    obj (object): object to return dictionary description  of
    """
    return obj.__dict__

