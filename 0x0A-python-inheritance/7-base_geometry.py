#!/usr/bin/python3
"""
Define a class with methods for geometry-related operations
"""


class BaseGeometry:
    """This class defines a geometry-related base class."""

    def area(self):
        """Raises an Exception with the message 'area() is not implemented'."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates the given value:
        If not an integer
            Raises a TypeError exception with the message '<name> must be an integer'.
        If less or equal to 0:
            Raises a ValueError exception with the message '<name> must be greater than 0'.
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
