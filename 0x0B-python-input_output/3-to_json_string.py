#!/usr/bin/python3
''' function that return the JSON  of an object (string)
'''

import json


def to_json_string(my_obj):
    ''' modul to_json_string
     Returns  representing Json
    '''
    return json.dumps(my_obj)
