#!/usr/bin/python3
"""
Script to add all arguments to
a Python list and save them to a file
"""

import sys
from 5-save_to_json_file import save_to_json_file
from 6-load_from_json_file import load_from_json_file

try:
    file_list = load_from_json_file("add_item.json")
except FileNotFoundError:
    file_list = []

file_list.extend(sys.argv[1:])
save_to_json_file(file_list, "add_item.json")
