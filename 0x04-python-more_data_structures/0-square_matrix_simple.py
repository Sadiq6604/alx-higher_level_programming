#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    my_matrix = []
    for x in matrix:
        my_matrix.append(list(map(lambda x: x**2, x)))
    return (my_matrix)
