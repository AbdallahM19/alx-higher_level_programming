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
    return (np.matmul(m_a, m_b))
