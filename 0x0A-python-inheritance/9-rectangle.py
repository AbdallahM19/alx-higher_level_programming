#!/usr/bin/python3
"""
Module containing the Rectangle class
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Rectangle class,
    inherits from BaseGeometry
    """

    def __init__(self, width, height):
        """
        Initialize a Rectangle instance
        """
        super().__init__()
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """Calculate the area of the Rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """Return a string representation of the Rectangle"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
