#!/usr/bin/python3
"""
Appends a string at the end of a text file (UTF8)
returns the number of characters added
"""


def append_write(filename="", text=""):
    """
    Appends a string to the end of a text file
    returns the number of characters added
    """
    with open(filename, mode="a", encoding="utf-8") as file:
        return file.write(text)
