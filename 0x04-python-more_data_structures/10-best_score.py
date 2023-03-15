#!/usr/bin/python3


def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    maxval = 0
    maxkey = None
    for k, b in a_dictionary.items():
        if v > maxval:
            maxval = b
            maxval = k
    return maxkey
