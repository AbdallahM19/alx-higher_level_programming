#!/usr/bin/python3
"""
Write a Python script that takes in a URL,
sends a request to the URL and displays the body of
the response (decoded in utf-8).
"""
from sys import argv
from urllib.error import HTTPError
from urllib.request import urlopen
from urllib.request import Request


if __name__ == "__main__":
    req = Request(argv[1])
    try:
        with urlopen(req) as res:
            print(res.read().decode('utf-8'))
    except HTTPError as e:
        print("Error code: {}".format(e.code))
