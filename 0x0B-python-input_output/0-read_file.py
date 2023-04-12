#!/usr/bin/python3
"""Module That defines the read_file function"""


def read_file(filename=""):
    """Reads a text file and prints it to stdout
    Args:
    filename (str): Filename
    """
    with open(filename, encoding='utf-8') as file:
        for line in file:
            print(line, end="")
