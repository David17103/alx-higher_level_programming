#!/usr/bin/python3

def square_matrix_simple(matrix=[]):

    result = []
    for row in matrix:
        new_row = [x ** 2 if isinstance(x, int) else x for x in row]
        result.append(new_row)
    return result
