#!/usr/bin/python3
"""
Module to perform matrix multiplication using NumPy.
"""

import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """
    Multiplies two matrices using NumPy.

    Args:
        m_a (list): The first matrix.
        m_b (list): The second matrix.

    Returns:
        numpy.ndarray: The resulting matrix.

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

    if not m_a:
        raise ValueError("m_a can't be empty")
    if not m_b:
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
    return np.dot(m_a, m_b)
