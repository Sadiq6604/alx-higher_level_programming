#!/usr/bin/python3
""" object is exactly an instance of the specified class
"""


def is_same_class(obj, a_class):
    """ considering of  class an object"""
    if type(obj) is a_class:
        return True
    return False

