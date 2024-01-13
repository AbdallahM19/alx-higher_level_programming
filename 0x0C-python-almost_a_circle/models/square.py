#!/usr/bin/python3
"""Square class"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class"""
    def __init__(self, size, x=0, y=0, id=None):
        """Call the super class with id, x, y, width and height"""
        self.id = None
        self.size = size
        self.x = x
        self.y = y
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ return [Square] (<id>) <x>/<y> - <size>"""
        return "[Square] ({}) {}/{} - {}".format(
          self.id, self.x, self.y, self.size
        )

    @property
    def size(self):
        """Getter and setter for size"""
        return self.width

    @size.setter
    def size(self, value):
        """Getter and setter for size"""
        self.width = value
        self.height = value
