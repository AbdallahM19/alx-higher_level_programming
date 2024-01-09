#!/usr/bin/python3
"""
Module to perform matrix multiplication.
"""


def matrix_mul(m_a, m_b):
    """
    Multiplies two matrices.

    Args:
        m_a (list): The first matrix.
        m_b (list): The second matrix.

    Returns:
        TypeError: m_a is not a list
        TypeError: m_b is not a list
        TypeError: If m_a or m_b is not a list of lists
        TypeError: If one element of list of lists is not int/float
        TypeError: If row of m_a or m_b are not the same size
        ValueError: If m_a or m_b is empty
        ValueError: If m_a and m_b cannot be multiplied

    Raises:
        TypeError: If m_a or m_b is not a list, is not a list of lists,
                   or contains elements that are not integers or floats.
        ValueError: If m_a or m_b is empty
                   or if the matrices can't be multiplied.
    """
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    if not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")
    if not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")

    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")

    if not all(isinstance(num, (int, float)) for i in m_a for num in i):
        raise TypeError("m_a should contain only integers or floats")
    if not all(isinstance(num, (int, float)) for i in m_b for num in i):
        raise TypeError("m_b should contain only integers or floats")

    if not all(len(i) == len(m_a[0]) for i in m_a):
        raise TypeError("each row of m_a must be of the same size")
    if not all(len(i) == len(m_b[0]) for i in m_b):
        raise TypeError("each row of m_b must be of the same size")

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    result = [
        [0 for _ in range(len(m_b[0]))] for _ in range(len(m_a))
    ]
    for i in range(len(m_a)):
        for j in range(len(m_b[0])):
            for n in range(len(m_b)):
                result[i][j] += m_a[i][n] * m_b[n][j]
    return result
