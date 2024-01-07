#!/usr/bin/python3
"""
function divided 2 integers
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a given divisor.

    Args:
        matrix (list of lists): The input matrix containing integers or floats.
        div (int or float): The divisor.

    Returns:
        list of lists: A new matrix with elements rounded to 2 decimal places.

    Raises:
        TypeError: If matrix is not a list of lists of integers or floats,
                   or if each row of the matrix does not have the same size.
        TypeError: If div is not a number (integer or float).
        ZeroDivisionError: If div is equal to 0.
    """
    if not all(
        isinstance(row, list) and
        all(isinstance(i, (int, float)) for i in row)
        for row in matrix
    ):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats"
        )
    if any(len(row) != len(matrix[0]) for row in matrix):
        raise TypeError(
            "Each row of the matrix must have the same size"
        )
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    return [[round(i / div, 2) for i in row] for row in matrix]
