#!/usr/bin/python3
'''
A function that return  an object
(Python data structure) repr by a
JSON string:
'''

import json


def from_json_string(my_str):
    '''
    Return object as JSON
    '''
    return json.loads(my_str)
