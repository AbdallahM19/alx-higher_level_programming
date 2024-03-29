#!/usr/bin/python3
"""
Write a Python script that
fetches https://alx-intranet.hbtn.io/status
"""
import urllib.request
import urllib.error


if __name__ == "__main__":
    new_req = urllib.request.Request("https://alx-intranet.hbtn.io/status")
    with urllib.request.urlopen(new_req) as response:
        i = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(i)))
        print("\t- content: {}".format(i))
        print("\t- utf8 content: {}".format(i.decode("utf-8")))
