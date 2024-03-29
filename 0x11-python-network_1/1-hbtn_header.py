#!/usr/bin/python3
"""
Write a Python script that takes in a URL,
sends a request to the URL and displays the value of
the X-Request-Id variable found in the header of the response.
"""
import urllib.request
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as res:
        request_id = dict(res.headers).get("X-Request-Id")
        print(request_id)
