#!/usr/bin/python3
"""Base class"""

import json


class Base:
    """my functions"""

    __nb_objects = 0

    def __init__(self, id=None):
        """class constructor"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation of list_dictionaries"""
        if list_dictionaries is None or not list_dictionaries:
            return []
        else:
            return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string representation"""
        if json_string is None or not json_string:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file"""
        file = cls.__name__ + ".json"
        with open(file, "w") as jsonfile:
            if list_objs is None:
                jsonfile.write("[]")
            else:
                list_dicts = [i.to_dictionary() for i in list_objs]
                jsonfile.write(cls.to_json_string(list_dicts))

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes"""
        if cls.__name__ == 'Rectangle':
            i = cls(1, 1)
        elif cls.__name__ == 'Square':
            i = cls(1)
        else:
            i = None
        i.update(**dictionary)
        return i

    @classmethod
    def load_from_file(cls):
        """returns a list of instances"""
        file = cls.__name__ + ".json"
        try:
            with open(file, "r") as jsonfile:
                content = jsonfile.read()
                if not content:
                    return []
                return [cls.create(**i) for i in cls.from_json_string(content)]
        except FileNotFoundError:
            return []
