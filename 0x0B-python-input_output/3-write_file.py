#!/usr/bin/python3
"""The module that  contains a function that writes a string to a text
    file (UTF8) and returns the number of characters written.
"""


def write_file(filename="", text=""):
    """writing a string to a text file (UTF8) and returns
        the number of characters are  written.
    Keyword Arguments:
        filename {str} -- file name (default: {""})
        text {str} -- text (default: {""})
    Returns:
        Int -- number of characters written
    """
    with open(filename, "w", encoding="utf-8") as file:
        return file.write(text)
