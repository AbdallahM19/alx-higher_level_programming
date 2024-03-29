#!/usr/bin/python3
"""
Write a Python script that takes in a URL and an email,
sends a POST request to the passed URL with the email
as a parameter, and displays the body of the response
(decoded in utf-8)
"""
import sys
from urllib.parse import urlencode
from urllib.request import Request
from urllib.request import urlopen


if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    data = urlencode({'email': email})
    req = Request(url, data.encode('ascii'))
    with urlopen(req) as response:
        i = response.read().decode('utf-8')
        print(i)
