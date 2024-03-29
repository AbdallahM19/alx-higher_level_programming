#!/usr/bin/python3
"""
Write a Python script that takes in a letter and
sends a POST request to
http://0.0.0.0:5000/search_user
with the letter as a parameter.
"""
import requests
from sys import argv


if __name__ == "__main__":
    if len(argv) == 1:
        q = ""
    else:
        q = argv[1]
    load = {'q': q}
    url = 'http://0.0.0.0:5000/search_user'
    res = requests.post(url, load)
    try:
        json_res = res.json()
        if json_res == {}:
            print("No result")
        else:
            print("[{}] {}".format(
                json_res.get('id'), json_res.get('name')
            ))
    except ValueError:
        print("Not a valid JSON")
