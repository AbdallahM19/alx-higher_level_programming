#!/usr/bin/python3
"""
Define a class with a method that raises an exception
"""


class BaseGeometry:
    """This class defines a geometry-related base class"""

    def area(self):
        """
        Raises an Exception with the message 'area() is not implemented'
        """
        raise Exception("area() is not implemented")
