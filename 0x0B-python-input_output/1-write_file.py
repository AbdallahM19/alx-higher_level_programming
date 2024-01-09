#!/usr/bin/python3
"""
Writes a string to a text file (UTF8)
returns the number of characters written
"""


def write_file(filename="", text=""):
    """
    Writes a string to a text file
    returns the number of characters written
    """
    with open(filename, "w", encoding="utf-8") as file:
        return file.write(text)
