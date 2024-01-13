#!/usr/bin/python3
"""Base class"""

from models.base import Base


class Rectangle(Base):
    """Rectangle class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Call the superclass constructor"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Getter and setter for width"""
        return self.__width

    @property
    def height(self):
        """Getter and setter for height"""
        return self.__height

    @property
    def x(self):
        """Getter and setter for x"""
        return self.__x

    @property
    def y(self):
        """Getter and setter for y"""
        return self.__y

    @width.setter
    def width(self, value):
        """Getter and setter for width"""
        if not isinstance(value, int):
            raise TypeError("Width must be an integer")
        if value <= 0:
            raise ValueError("Width must be > 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """Getter and setter for height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @x.setter
    def x(self, value):
        """Getter and setter for x"""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @y.setter
    def y(self, value):
        """Getter and setter for y"""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """returns the area value of the Rectangle instance"""
        return self.height * self.width

    def display(self):
        """
        prints in stdout the Rectangle instance with the character #
        """
        for _ in range(self.y):
            print()
        for _ in range(self.height):
            print(' ' * self.x + '#' * self.width)

    def __str__(self):
        """returns [Rectangle] (<id>) <x>/<y> - <width>/<height>"""
        return "[{}] ({}) {}/{} - {}/{}".format(
          'Rectangle', self.id, self.__x, self.__y, self.__width, self.__height
        )

    def update(self, *args, **kwargs):
        """assigns an argument to each attribute"""
        if args:
            for i in range(len(args)):
                if i == 0:
                    self.id = args[0]
                elif i == 1:
                    self.width = args[1]
                elif i == 2:
                    self.height = args[2]
                elif i == 3:
                    self.x = args[3]
                elif i == 4:
                    self.y = args[4]
        elif kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """returns the dictionary representation of a Rectangle"""
        rect_dict = {
            'id' : self.id,
            'width' : self.width,
            'height' : self.height,
            'x' : self.x,
            'y' : self.y
        }
        return(rect_dict)
