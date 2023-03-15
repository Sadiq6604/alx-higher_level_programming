#!/usr/bin/python3


def print_sorted_dictionary(a_dictionary):
    for b in sorted(a_dictionary.keys()):
        print("{}: {}".format(b, a_dictionary[b]))
