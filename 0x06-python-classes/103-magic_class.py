#!/usr/bin/python3
"""
Define
my square
"""
import math


class MagicClass:
    """My Private instance attribute"""

    def __init__(self, radius=0):
        self.__radius = 0
        self.radius = radius

    @property
    def radius(self):
        return self.__radius

    @radius.setter
    def radius(self, value):
        if type(value) is not int and type(value) is not float:
            raise TypeError("radius must be a number")
        self.__radius = value

    def area(self):
        return math.pi * self.__radius**2

    def circumference(self):
        return math.pi * self.__radius * 2
