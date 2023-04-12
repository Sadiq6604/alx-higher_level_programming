#!/usr/bin/python3
"""The module defined  number_of_lines function"""


def number_of_lines(filename=""):
    """Return number of line of a text file
    Args:
    filename (str): Filename
    """
    count = 0
    with open(filename, encoding='utf-8') as file:
        for line in file:
            count += 1
        return count
