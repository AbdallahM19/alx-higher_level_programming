#!/usr/bin/python3
"""Base class"""

import json
import csv


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

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Serialize instances to CSV file"""
        filename = cls.__name__ + ".csv"
        with open(filename, "w", newline='') as csvfile:
            if list_objs is not None or list_objs != []:
                header = cls.get_csv_header()
                csv_line = csv.DictWriter(csvfile, fieldnames=header)
                for obj in list_objs:
                    csv_line.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """Deserialize instances from CSV file"""
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, "r", newline="") as csvfile:
                header = cls.get_csv_header()
                lines = csv.DictReader(csvfile, fieldnames=header)
                lines = [
                  dict([k, int(v)] for k, v in d.items()) for d in lines
                ]
                return [cls.create(**i) for i in lines]
        except (FileNotFoundError, IOError):
            return []

    @classmethod
    def get_csv_header(cls):
        """Get CSV header for the class"""
        if cls.__name__ == "Rectangle":
            return ["id", "width", "height", "x", "y"]
        else:
            return ["id", "size", "x", "y"]
