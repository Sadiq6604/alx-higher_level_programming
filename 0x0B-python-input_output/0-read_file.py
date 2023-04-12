#!/usr/bin/python3
'''
a function that reads a text file (UTF8)
and prints it as stdout
'''


def read_file(filename=""):
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            print(line, end='')
    f.close()
