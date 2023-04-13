#!/usr/bin/python3
"""module that creates an Object from a JSON files"""


import json


def load_from_json_file(filename):
    """creates an Object from a JSON file
    Args:
    filename (str): JSON file to create an Object from
    Returns:
    object: JSON object
    """
    with open(filename, encoding='utf-8') as file:
        return json.loads(file.read()
