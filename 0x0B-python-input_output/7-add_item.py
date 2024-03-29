#!/usr/bin/python3
"""Script to add all arguments to a Python list and save them to a file"""

import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

try:
    myfile = load_from_json_file("add_item.json")
except FileNotFoundError:
    myfile = []
myfile.extend(sys.argv[1:])
save_to_json_file(myfile, "add_item.json")
