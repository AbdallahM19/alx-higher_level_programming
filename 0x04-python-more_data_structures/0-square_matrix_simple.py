#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new = matrix.copy()
    for i in range(len(matrix)):
        new[i] = list(map(lambda num: num ** 2, matrix[i]))
    return (new)
