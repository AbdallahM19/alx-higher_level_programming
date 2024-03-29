#!/usr/bin/python3
"""
Write a Python script that takes your GitHub
credentials (username and password) and
uses the GitHub API to display your id
"""
import requests
from sys import argv
from requests.auth import HTTPBasicAuth

if __name__ == "__main__":
    basic_auth = HTTPBasicAuth(argv[1], argv[2])
    url = "https://api.github.com/user"
    res = requests.get(url, auth=basic_auth)
    i = res.json().get("id")
    print(i)
