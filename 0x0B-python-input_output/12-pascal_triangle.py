#!/usr/bin/python3
"""Pascal Triangle Module"""


def pascal_triangle(n):
    """Return a list of list of integers repr Pascal Triangle of n"""

    ans = []
    if n > 0:
        ans.append([1])
        for r in range(1, n):
            prv = ans[-1]
            ans.append([1] + [prv[i - 1] + prv[i] for i in range(1, r)] + [1])
    return ans
