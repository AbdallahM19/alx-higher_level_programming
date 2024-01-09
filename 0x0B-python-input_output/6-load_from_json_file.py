#!/usr/bin/python3
"""
Creates an Object from a “JSON file”
"""

import json


def load_from_json_file(filename):
    """
    Creates an object from a JSON file
    """
    with open(filename, encoding="utf-8") as file:
        return json.load(file)
