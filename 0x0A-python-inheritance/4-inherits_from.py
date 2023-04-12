#!/usr/bin/python3
"""
    inherits_all
"""


def inherits_from(obj, a_class):
    """
    function that returns True if the object is an instance
    of a class that inherited (directl or indirectly)
    from the specified class ; otherwise False.
    """
    return issubclass(type(obj), a_class) and type(obj) is not a_class
