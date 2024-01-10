#!/usr/bin/python3
"""
Defines a Student class
"""


class Student:
    """
    Represents a student with first_name, last_name, and age
    """

    def __init__(self, first_name, last_name, age):
        """
        Initializes a new Student instance
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of a Student instance
        """
        if attrs is None or not isinstance(attrs, list):
            return self.__dict__
        else:
            return {
                key: getattr(self, key) for key in attrs if hasattr(self, key)
            }
